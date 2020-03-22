# uncompyle6 version 3.2.6
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.6 (default, Mar 29 2019, 00:03:27) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-36)]
# Embedded file name: app\api\settings.py
"""
提供数据设置API
"""
from cmp.db.mongodb import DB
setting_table_instance = DB('settings')

class l11l111ll_wcplus_:

    def __int__(self):
        pass

    def get(self):
        """
        :return: 获取所有的设置字段{}
        """
        sd = setting_table_instance.get()
        datas_dict = {}
        for s in sd:
            datas_dict[s['key']] = s['value']

        from cmp.protect import Passport
        from utils.network import getLocalIp
        datas_dict['uuid'] = Passport.getUUid()
        passport_expire_time = Passport.examplePassport()
        if not passport_expire_time:
            datas_dict['passport'] = 0
        else:
            datas_dict['passport'] = passport_expire_time
        datas_dict['proxy_server'] = getLocalIp()
        return datas_dict

    def insert(self, l11l1111l_wcplus_):
        """
        :param settings_data_dict: settings数据本质上是一个字典
        :return: 插入或修改
        """
        l11l11111_wcplus_ = []
        for key in l11l1111l_wcplus_:
            item = {}
            item['key'] = key
            item['value'] = l11l1111l_wcplus_[key]
            l11l11111_wcplus_.append(item)

        setting_table_instance.insert('key', l11l11111_wcplus_)

    def delete(self, key, all=False):
        """
        :param key:准确的key
        :param all:
        :return:
        """
        if all:
            setting_table_instance.delete()
        else:
            setting_table_instance.delete(key=key)