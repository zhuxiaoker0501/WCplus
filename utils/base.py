# uncompyle6 version 3.2.6
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.6 (default, Mar 29 2019, 00:03:27) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-36)]
# Embedded file name: utils\base.py
from loguru import logger
import pprint
pp = pprint.PrettyPrinter(depth=6)
prettyPrint = pp.pprint

def windowFileConvert(file_name):
    """
    :param file_name:等待验证的文件名
    :return: 验证windows文件名的合法性 将不合法的字符替换为 下划线_
    """
    import re
    flag = '[\\/\\\\\\:\\*\\?\\"\\<\\>\\|\\“\\”]'
    converted_file = re.sub(flag, '_', file_name)
    return converted_file


def osVersion():
    from sys import platform
    if platform == 'linux' or platform == 'linux2':
        return 'linux'
    if platform == 'darwin':
        return 'osx'
    if platform == 'win32':
        return 'win'