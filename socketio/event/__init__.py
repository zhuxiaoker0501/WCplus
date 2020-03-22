# uncompyle6 version 3.2.6
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.6 (default, Mar 29 2019, 00:03:27) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-36)]
# Embedded file name: l1l11_wcplus_\event\__init__.py
"""
websocket事件监听
"""
from socketio import socketio

@socketio.on('connect')
def l1ll11111l1_wcplus_():
    socketio.emit('connect', {'data': 'hand shake'})


@socketio.on('hello')
def l1l1lllllll_wcplus_(data):
    print(data)


@socketio.on('pause')
def l1ll111111l_wcplus_(data):
    from instance import crawler_manager
    if data:
        crawler_manager.stop()
    else:
        crawler_manager.start()


@socketio.on('ask_data')
def l1ll1111l11_wcplus_(data):
    if data == 'req_data':
        from app.api.prepare_data_for_front_end import PrepareDataForFrontEnd
        PrepareDataForFrontEnd().send()
    try:
        import builtins
        builtins.crawler_process.sendProcess()
    except:
        pass


@socketio.on('export_excel')
def l1ll11111ll_wcplus_(nickname):
    nickname = (nickname.encode(encoding='raw_unicode_escape')).decode('utf-8')
    from app.export.excel import l111l1ll1_wcplus_
    l111l1ll1_wcplus_(nickname).run()


@socketio.on('delete_gzh')
def l1l1llllll1_wcplus_(nickname):
    nickname = (nickname.encode(encoding='raw_unicode_escape')).decode('utf-8')
    from app.api.delete import DeleteGZH
    DeleteGZH(nickname).run()


@socketio.on('command')
def l1l1lllll1l_wcplus_(command):
    command = (command.encode(encoding='raw_unicode_escape')).decode('utf-8')
    from app.command_handler import execute_command
    execute_command(command)