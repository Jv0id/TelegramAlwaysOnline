# -*- coding: utf-8 -*-

import asyncio

from login import client, main

if __name__ == '__main__':
    # 获取当前事件循环
    loop = asyncio.get_event_loop()
    with client:
        loop.run_until_complete(main())