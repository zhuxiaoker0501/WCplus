# uncompyle6 version 3.2.6
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.6 (default, Mar 29 2019, 00:03:27)
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-36)]
# Embedded file name: cmp\processFunc\__init__.py
"""
代理服务器模块
"""
from mitmproxy import proxy, options
from mitmproxy.tools.dump import DumpMaster
from cmp.mitmproxy.addons import ParseFlow

def proxyMaster():
    flow_instance = ParseFlow()
    opts = options.Options(listen_host='0.0.0.0', listen_port=8080)
    proxy_config = proxy.config.ProxyConfig(opts)
    m = DumpMaster(opts)
    m.server = proxy.server.ProxyServer(proxy_config)
    m.addons.add(flow_instance)
    try:
        m.run()
    except KeyboardInterrupt:
        print('')
        m.shutdown()


if __name__ == '__main__':
    proxyMaster()
