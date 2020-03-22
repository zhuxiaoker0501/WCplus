# uncompyle6 version 3.2.6
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.6 (default, Mar 29 2019, 00:03:27) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-36)]
# Embedded file name: instance\__init__.py
"""
定义全局对象
"""
from cmp.db.mongodb import DB
crawler_log_table_instance = DB('crawler_log')
req_data_table_instance = DB('req_data')
from app.crawl_manag.params_handle import HandleParam
rd = HandleParam()
from app.api.settings import l11l111ll_wcplus_
l1l1111ll_wcplus_ = l11l111ll_wcplus_()
from app.crawl_manag import CrawlManage
crawler_manager = CrawlManage()
from utils.base import osVersion
os_version = osVersion()