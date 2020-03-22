# Python bytecode 3.6 (3372)
# Embedded file name: main.py
# Decompiled by https://python-decompiler.com
"""

"""
from threading import Thread
from multiprocessing import Process
import multiprocessing
from socketio import socketIo
from cmp.mitmproxy import proxyMaster
import webbrowser, time

def processFunc():
    """
    :return:
    """
    proxyMaster()


def threadFunc():
    """
    :return:
    """
    from app.api.prepare_data_for_front_end import PrepareDataForFrontEnd
    while True:
        PrepareDataForFrontEnd().send()
        time.sleep(3)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    Process(target=processFunc).start()
    Thread(target=threadFunc).start()
    webbrowser.open('http://localhost:5000')
    socketIo()
