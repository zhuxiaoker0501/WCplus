# uncompyle6 version 3.2.6
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.6 (default, Mar 29 2019, 00:03:27) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-36)]
# Embedded file name: l1l11_wcplus_\router\__init__.py
"""
页面路由
"""
from socketio import app_instance
from flask import render_template, send_from_directory
from instance import os_version

@app_instance.route('/', methods=['GET'])
def index():
    """
    :return: 返回首页
    """
    return render_template('index.html')


@app_instance.route('/img/<filename>', methods=['GET'])
def l1l1llll11l_wcplus_(filename):
    """
    :param filename:
    :return: 返回一个静动态文件
    """
    print(filename)
    return send_from_directory(directory='web_server/static/img/', filename=filename)


@app_instance.route('/html/<nickname>/<md5>', methods=['GET'])
def l1l1llll1ll_wcplus_(nickname, md5):
    """
    :param filename:
    :return: 返回一个静动态文件
    """
    from cmp.db.mongodb import DB
    if DB(nickname).count(id=md5, comment_id={'$exists': True}):
        from webbrowser import open
        import os
        if os_version == 'win':
            file_name = os.getcwd() + '\\\\web_server\\\\static\\\\html\\\\' + nickname + '\\' + md5 + '.html'
            if os.path.isfile(file_name):
                open(file_name)
            else:
                return '找不到该文章 可能是没有迁移到新版本的WCplus 请先从旧版本的WCplus中复制或移动到新版本的WCplus的web_server/static/html目录下'
        else:
            file_name = os.getcwd() + '/web_server/static/html/' + nickname + '/' + md5 + '.html'
            if os.path.isfile(file_name):
                open('file://' + file_name)
            else:
                return '找不到该文章 可能是没有迁移到新版本的WCplus 请先从旧版本的WCplus中复制或移动到新版本的WCplus的web_server/static/html目录下'
            return ('', 204)
        return '未保存该文章 请先采集'