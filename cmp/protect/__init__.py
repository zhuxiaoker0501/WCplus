# uncompyle6 version 3.2.6
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.6 (default, Mar 29 2019, 00:03:27) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-36)]
# Embedded file name: cmp\protect\__init__.py
from utils.base import logger
from utils.time import getBaiduTime
from datetime import datetime

def getUuidIp():
    """
    :return: (UUID, ip)
    用该方法的返回的IP地址似乎有问题
    """
    from psutil import net_if_addrs
    from instance import os_version
    res = []
    for k, v in net_if_addrs().items():
        for item in v:
            address = item[1]
            if os_version == 'win':
                if '-' in address and len(address) == 17:
                    res.append(int(address.replace('-', ''), 16))
                else:
                    if os_version == 'osx' and ':' in address and len(address) == 17:
                        res.append(int(address.replace(':', ''), 16))

    return res


class Passport:

    @classmethod
    def getUUid(cls):
        uuid = getUuidIp()
        if len(uuid):
            return uuid[0]
        else:
            return 1

    @classmethod
    def examplePassport(cls, q=True):
        mac, pt = cls.getMacUUid()
        if not mac and not pt:
            return False
        else:
            uuid_ = cls.getUUid()
            mac_uuid = getUuidIp()
            if uuid_ == 1:
                return False
            if int(mac) not in mac_uuid:
                if not q:
                    logger.warning('证书错误')
                return False
            end_time = int(pt) - int(mac) - 12874767561234
            baidu_time = getBaiduTime()
            if not baidu_time:
                return False
            time_left = end_time - getBaiduTime()
            if time_left <= 0:
                if not q:
                    logger.warning('证书过期')
                return False
            end_time = datetime.utcfromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')
            if not q:
                logger.info('证书有效至' + end_time)
            return end_time

    @classmethod
    def getMacUUid(cls):
        try:
            data = None
            with open('./license.ca', 'r', encoding='utf-8') as (f):
                data = f.readlines()
            mac = int(data[70][:-1])
            uuid = int(data[91][:-1])
            return ( mac, uuid)
        except:
            logger.warning('未能找到授权证书license.ca')
            return (None, None)


if __name__ == '__main__':
    print(getUuidIp())