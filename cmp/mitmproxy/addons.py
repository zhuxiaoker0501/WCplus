# uncompyle6 version 3.2.6
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.6 (default, Mar 29 2019, 00:03:27) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-36)]
# Embedded file name: cmp\processFunc\addons.py
"""
自定义mimproxy脚本 详细见 https://docs.mitmproxy.org/stable/addons-overview/
由于使用anyproxy的历史原因 这里会解析mitmproxy代理数据为anyproxy同样的格式
"""
import json
from utils.string_handle import string2Dict
from utils.base import logger, prettyPrint
from datetime import datetime
from instance import req_data_table_instance

wxuin_value = None

event_url_maps = {'load_more': 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg',
                 'getappmsgext':'https://mp.weixin.qq.com/mp/getappmsgext?',
                 'appmsg_comment':'https://mp.weixin.qq.com/mp/appmsg_comment?action=getcomment',
                 'content':'https://mp.weixin.qq.com/s?',
                 'home':'https://mp.weixin.qq.com/mp/profile_ext?action=home'}

def insertDataToDb(key, value):
    value = str(value).replace("'", '"')
    data = {'id':key,  'key':key,  'time':datetime.now(),  'value':value}
    req_data_table_instance.insert('id', data)


class ParseFlow:
    """
    拦截url_filter中的请求参数 用wxuin.key.req的格式作为key name 存入数据库
    """

    @staticmethod
    def parseWxuin(req_data):
        """
        :param req_data:
        :return: 微信特有 从cookie中解析出wxuin
        """
        wxuin_value = 'UNK'
        if 'Cookie' in req_data['requestOptions']['headers']:
            cookie_dict = string2Dict(req_data['requestOptions']['headers']['Cookie'], ';', '=')
        else:
            cookie_dict = string2Dict(req_data['requestOptions']['headers']['cookie'], ';', '=')
        if 'wxuin' in cookie_dict:
            wxuin_value = cookie_dict['wxuin']
        return wxuin_value

    def request(self, flow):
        pass

    def response(self, flow):
        global wxuin_value
        for key in event_url_maps:
            if event_url_maps[key] in flow.request.url:
                anyproxy_format_request, timestamp = ParseFlow2Anyproxy.convertFlow2Anyproxy(flow.request)
                if key == 'home':
                    wxuin_value = self.parseWxuin(anyproxy_format_request)
                if wxuin_value == 'UNK':
                    return
                key_name = '%s.%s.req' % (wxuin_value, key)
                insertDataToDb(key_name, anyproxy_format_request)
                logger.debug(key_name)
            if key == 'getappmsgext':
                status_code, text = ParseFlow2Anyproxy.get_response(flow.response)
                json_value = json.loads(text)
                # nick_name = 'UNK'
                if 'nick_name' in json_value:
                    nick_name = json_value['nick_name']
                    if nick_name == 'UNK':
                        logger.debug('没能找到微信昵称 换一篇文章点击试试看 确保文章底部阅读数据出现')
                    else:
                        insertDataToDb(nick_name + '.nick_name', wxuin_value)
            elif key == 'home':
                status_code, resp_text = ParseFlow2Anyproxy.get_response(flow.response)
                gzh_name = resp_text.split('var nickname = "')[1].split('" || ""')[0]
                logger.info('准备公众号:' + gzh_name)
                insertDataToDb('current_nickname', gzh_name)


class ParseFlow2Anyproxy:
    """
    解析flow数据 成为anyrpoxy格式
    """

    @staticmethod
    def convertFlow2Anyproxy(request):
        """
        :param request:
        :return: 模拟anyrpoxy 格式化请求数据
        """
        result = {}
        result['protocol'] = request.scheme
        result['url'] = request.url
        result['requestOptions'] = {}
        result['requestOptions']['headers'] = ParseFlow2Anyproxy.parseHeader(request.headers)
        result['requestOptions']['hostname'] = request.pretty_host
        result['requestOptions']['port'] = request.port
        result['requestOptions']['path'] = request.path
        result['requestOptions']['method'] = request.method
        result['requestData'] = request.text
        timestamp = int(request.timestamp_end * 1000)
        return (
         result, timestamp)

    @staticmethod
    def get_response(response):
        """
        :param response:
        :return: 返回响应码和响应体
        """
        return (
         response.status_code, response.text)

    @staticmethod
    def parseHeader(headers):
        result = {}
        for i in headers.fields:
            result[str(i[0], 'utf-8')] = str(i[1], 'utf-8')

        if ':authority' in result:
            result.pop(':authority')
        return result