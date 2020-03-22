# uncompyle6 version 3.2.6
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.6 (default, Mar 29 2019, 00:03:27) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-36)]
# Embedded file name: l1l11_wcplus_\__init__.py
from flask import Flask
from flask_socketio import SocketIO
from flask_restful import Api
from flask_cors import CORS
import logging
logging.getLogger('socketio').setLevel(logging.ERROR)
logging.getLogger('engineio').setLevel(logging.ERROR)
logging.getLogger('werkzeug').setLevel(logging.ERROR)
app_instance = Flask('WCplus', template_folder='./web_server/static', static_folder='./web_server/static')
CORS(app_instance, resources={'/api/*': {'origins': '*'}})

from socketio.api import api_url_map
api = Api(app_instance)
for item in api_url_map:
    api.add_resource(item['res'], '/api' + item['url'])

socketio = None
from instance import os_version
if os_version == 'osx':
    socketio = SocketIO(app_instance, l1ll11ll1ll_wcplus_=False)
else:
    if os_version == 'win':
        try:
            socketio = SocketIO(app_instance, async_mode='gevent', l1ll11ll1ll_wcplus_=False)
        except:
            socketio = SocketIO(app_instance, l1ll11ll1ll_wcplus_=False)

        from socketio.router import *
        from socketio.event import *

def socketIo():
    socketio.run(app_instance, host='0.0.0.0', port=5000)