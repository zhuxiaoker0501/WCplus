# uncompyle6 version 3.2.6
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.6 (default, Mar 29 2019, 00:03:27) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-36)]
# Embedded file name: l1l11_wcplus_\api\__init__.py
"""
RESTful API
"""
from socketio.api.hello_flask_api import HelloFlaskApi
from socketio.api.l1lll1_wcplus_ import CrawlFlaskAPi
from socketio.api.l11lll1l1_wcplus_ import l1ll111ll11_wcplus_
from socketio.api.settings import l11l111ll_wcplus_
from socketio.api.search import l1lll11lll_wcplus_

api_url_map = [
 {'res':HelloFlaskApi, 'url': '/helloworld'},
 {'res':CrawlFlaskAPi, 'url': '/crawler'},
 {'res':l1ll111ll11_wcplus_, 'url':'/gzh'},
 {'res':l11l111ll_wcplus_, 'url':'/settings'},
 {'res':l1lll11lll_wcplus_, 'url':'/search'}
]