# -*- coding: utf-8 -*-
import asyncio
import logging
import os

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.account import UpdateStatusRequest

logging.basicConfig(level=logging.INFO)

API_ID = os.environ.get("api_id") or 123
API_HASH = os.environ.get("api_hash") or "123"

PHONE_NUMBER = os.environ.get("phone") or "+8613838381438"

if API_ID == 123 or API_HASH == '123' or PHONE_NUMBER == '+8613838381438':
    logging.fatal(
        "You must assign a api_id and api_hash and phone before using this script! 在登录前你必须给定ID和HASH和PHONE_NUMBER! 信息不会被保存！")

client = TelegramClient('session_name', API_ID, API_HASH)


async def check_login():
    await client.start()
    me = await client.get_me()
    print(f'Logged in as: {me.first_name}')


async def auto_login():
    try:
        await client.start()
        print("Successfully logged in.")
    except SessionPasswordNeededError:
        print("Two-step verification is enabled. Please enter your password.")
        password = input("Password: ")
        await client.sign_in(PHONE_NUMBER, password)


async def main():
    await client.start()
    if await client.is_user_authorized():
        while True:
            try:
                await client(UpdateStatusRequest(offline=False))
                me = await client.get_me()
                print(f'Logged in as: {me.first_name}')
                await asyncio.sleep(60)
                logging.info("Sleep for 1 min")
            except Exception as e:
                print(f'Not logged in: {e}. Attempting to log in...')
                await auto_login()
    else:
        await auto_login()
