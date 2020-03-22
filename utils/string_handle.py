# uncompyle6 version 3.2.6
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.6 (default, Mar 29 2019, 00:03:27) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-36)]
# Embedded file name: utils\string_handle.py


def string2Dict(s, join_char='\n', split_char=':'):
    """
    字符串到字典 支持自定义键值间隔符和成员间隔符
    :param s: 原字符串
    :param join_symbol: 连接符
    :param split_symbol: 分隔符
    :return: 字典
    """
    lines = s.split(join_char)
    data = dict()
    for item in lines:
        item = item.strip()
        if item:
            k, v = item.split(split_char, 1)
            data[k] = v.strip()

    return data


def dict2String(data, split_char='&', join_char='='):
    """
    :param data:dict数据
    :param join_symbol:不同成员之间的连接符
    :param split_symbol:名称和值分隔符
    :return: 字典转换为字符串
    """
    s = ''
    for k in data:
        s += str(k) + join_char + str(data[k]) + split_char

    return s[:-1]


def updateDictValue(whole_dict, part_dict, keys=None):
    """
    :param whole_dict:
    :param part_dict:
    :param keys:
    :return:根据指定的keys 用part_dict的value更新whole_dict的value
    """
    if keys == None:
        whole_dict.update(part_dict)
        return whole_dict
    for key in keys:
        if key in part_dict:
            whole_dict[key] = part_dict[key]

    return whole_dict


import hashlib

def encryptString(data):
    """
    由于hash不处理unicode编码的字符串（python3默认字符串是unicode）
        所以这里判断是否字符串，如果是则进行转码
        初始化md5、将url进行加密、然后返回加密字串
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    md5_code = hashlib.md5()
    md5_code.update(data)
    return md5_code.hexdigest()