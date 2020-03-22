# uncompyle6 version 3.2.6
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.6 (default, Mar 29 2019, 00:03:27) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-36)]
# Embedded file name: app\l1ll11ll1_wcplus_\l1l1lllll_wcplus_\__init__.py
"""
调度和管理爬虫 采集完成一个公众号的全部历史文章列表
"""
from app.crawl_manag.history_article_list.l1lll1_wcplus_ import Crawler
from instance import rd, crawler_log_table_instance
from cmp.db.mongodb import DB
from utils.base import logger, prettyPrint
from datetime import datetime
from instance import crawler_manager
import time

class CrawlHistoryAricleList:
    """
    优雅地拿下一个公众号的全部历史文章列表
    如果有必要直接调用自动操作手机的方法
    采集完毕之后结束对象的生命周期
    """

    def __init__(self):
        self.articles_detail = rd.articles_detail()
        self.nickname = self.articles_detail[0]['nickname']
        self.delay_criterion = 2.0
        self.length = len(self.articles_detail)
        self.delay = round(self.delay_criterion / self.length, 3)
        self.length = 0
        self.length = 0
        self.data = []
        self.nickname_table = DB(self.nickname)
        self.time_now = time.time()

    def parseHandleArticleList(self, filter=None, process=None):
        """
        :param filter: 过滤器比如按照时间过滤 按照数量过滤
        :param process: 前端进度显示实例
        :return: 轮流调用list中的微信 获取所有的历史文章列表
        """
        offset = 0
        flag = 1
        cnt = 0
        if 'load_more' in self.articles_detail[0]:
            while flag:
                while time.time() - self.time_now <= self.delay:
                    time.sleep(0.05)

                self.time_now = time.time()
                article_list = Crawler(offset, self.articles_detail[cnt % self.length]).run()
                article_list = self.check(article_list, offset, cnt)
                flag = int(article_list['des']['can_msg_continue'])
                offset = int(article_list['des']['next_offset'])
                cnt += 1
                self.data = article_list['data']
                self.length += len(self.data)
                flag = self.checkFIlter(filter)
                self.length += len(self.data)
                crawler_log_table_instance.insert('id', {'id':self.nickname, 'num':self.length, 'nickname':self.nickname, 'time':datetime.now()})
                process.reportCrawlNum(self.length)
                if self.save(self.data) == 'UPDATE':
                    break
                if not flag:
                    break
                time.sleep(self.delay)

        else:
            logger.warning('没有上滑加载更多历史文章')

    def save(self, l1l11111ll_wcplus_):
        """
        :return: 保存数据
        """
        res = None
        res = self.nickname_table.insert('id', l1l11111ll_wcplus_)
        return res

    def checkFIlter(self, filter):
        """
        :param filter:
        :return: 根据过滤器中的条件 决定继续还是结束文章列表的采集 True继续 false停止
        """
        if filter['type'] == 'true':
            if int(filter['num']) == 0:
                return True
            if self.length >= int(filter['num']):
                return False
            return True
        else:
            l11ll1llll_wcplus_ = []
            res = True
            for a in self.data:
                l11ll1l1l1_wcplus_ = a['p_date'].timestamp()
                if l11ll1l1l1_wcplus_ >= filter['start_time'] and l11ll1l1l1_wcplus_ <= filter['end_time']:
                    l11ll1llll_wcplus_.append(a)
                elif l11ll1l1l1_wcplus_ < filter['start_time']:
                    res = False

            self.data = l11ll1llll_wcplus_
            return res

    def check(self, flag, offset, cnt):
        """
        :param list_data: 请求返回的结果
        :param offset:
        :return: 带着本次请求的参数和结果一起过安检
        请求失败导致安检不通过 安检提醒人重新操作手机 操作完之后再次发起请求
        不排除还是会失败  继续调用自己
        """
        if flag != 'req_data_error':
            crawler_manager.check({'crawler': '历史文章列表', 'msg': 'success'})
        else:
            crawler_manager.check({'crawler': '历史文章列表', 'msg': 'req_data_error'})
            self.articles_detail = rd.articles_detail()
            while len(self.articles_detail) == 0:
                self.articles_detail = rd.articles_detail()
                from utils.front import sendNotification
                sendNotification('没有发现参数', '参数错误', _type='error')
                time.sleep(3)

            flag = Crawler(offset, self.articles_detail[0]).run()
            self.check(flag, offset, cnt)
        return flag