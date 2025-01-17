# -*- coding: utf-8 -*-

import logging
from login import client
from telethon.tl.functions.account import UpdateStatusRequest
import time

if __name__ == '__main__':
    if client.is_user_authorized():
        logging.info("You are now AlwaysOnline™, Yah!")
        while True:
            client(UpdateStatusRequest(offline=False))
            time.sleep(60)
            logging.debug("Sleep for 1 min")
    else:
        logging.fatal("Login Fails, please retry... 失败，请重试！")
