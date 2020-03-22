# uncompyle6 version 3.2.6
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.6 (default, Mar 29 2019, 00:03:27) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-36)]
# Embedded file name: app\command_handler\l111ll1ll_wcplus_.py
"""
run 方法必须
"""
from utils.front import l111lll11_wcplus_

class l111ll1l1_wcplus_:

    def __int__(self):
        pass

    def run(self, command, l111llll1_wcplus_):
        import time
        begin_time = time.time()
        print(command, l111llll1_wcplus_)
        from instance import crawler_log_table_instance
        l1l1l1lll_wcplus_ = crawler_log_table_instance.get()
        l111lll1l_wcplus_ = []
        for g in l1l1l1lll_wcplus_:
            l111lll1l_wcplus_.append(g['nickname'])

        if len(l111llll1_wcplus_) and set(l111llll1_wcplus_) <= set(l111lll1l_wcplus_):
            l111lll1l_wcplus_ = l111llll1_wcplus_
        for nickname in l111lll1l_wcplus_:
            l111lll11_wcplus_('> 搜集文章正文 %s' % nickname)
            from app.crawl_manag.article import l1ll1111l_wcplus_
            l1ll1111l_wcplus_(nickname, l1ll11lll_wcplus_=128)
            l111lll11_wcplus_('>> 创建索引 服务搜索 %s' % nickname)
            from app.api.prepare_data_for_front_end import sendNotificationMsg
            sendNotificationMsg(nickname)
            l111lll11_wcplus_('>>> 完成 %s' % nickname)

        l111lll11_wcplus_('指令完成 用时%.1f分钟' % ((time.time() - begin_time) / 60))