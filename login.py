# -*- coding: utf-8 -*-
import logging
import os
import sys

from telethon import TelegramClient, utils
from telethon.errors import SessionPasswordNeededError, PhoneNumberOccupiedError, PhoneNumberUnoccupiedError, \
    PhoneCodeEmptyError, PhoneCodeExpiredError, PhoneCodeInvalidError, PhoneCodeHashEmptyError

logging.basicConfig(level=logging.INFO)

api_id = os.environ.get("api_id") or "123"
api_hash = os.environ.get("api_hash") or "123"

phone = os.environ.get("phone") or "+8613838381438"
password = os.environ.get("password") or "123"

if api_id == '123' or api_hash == '123' or password == '123':
    logging.fatal(
        "You must assign a API and password before using this script! 在登录前你必须给定ID和HASH和密码! 密码不会被保存！")

logging.info("Trying to Login to Telegram... 正在尝试登录...")
client = TelegramClient('session_file', api_id, api_hash, spawn_read_thread=False)
client.connect()


def start(self=client,
          phone=phone,
          password=password,
          bot_token=None, force_sms=False, code_callback=None,
          first_name='New User', last_name=''):
    if code_callback is None:
        def code_callback():
            return input('Please enter the code you received: ')
    elif not callable(code_callback):
        raise ValueError(
            'The code_callback parameter needs to be a callable '
            'function that returns the code you received by Telegram.'
        )

    if not phone and not bot_token:
        raise ValueError('No phone number or bot token provided.')

    if phone and bot_token and not callable(phone):
        raise ValueError('Both a phone and a bot token provided, '
                         'must only provide one of either')

    if not self.is_connected():
        self.connect()

    if self.is_user_authorized():
        self._check_events_pending_resolve()
        return self

    if bot_token:
        self.sign_in(bot_token=bot_token)
        return self

    # Turn the callable into a valid phone number
    while callable(phone):
        phone = utils.parse_phone(phone) or phone

    me = None
    attempts = 0
    max_attempts = 3
    two_step_detected = False

    sent_code = self.send_code_request(phone, force_sms=force_sms)
    sign_up = not sent_code.phone_registered
    while attempts < max_attempts:
        try:
            if sign_up:
                me = self.sign_up(code_callback(), first_name, last_name)
            else:
                me = self.sign_in(phone, code_callback())
            break
        except SessionPasswordNeededError:
            two_step_detected = True
            break
        except PhoneNumberOccupiedError:
            sign_up = False
        except PhoneNumberUnoccupiedError:
            sign_up = True
        except (PhoneCodeEmptyError, PhoneCodeExpiredError,
                PhoneCodeHashEmptyError, PhoneCodeInvalidError):
            print('Invalid code. Please try again.', file=sys.stderr)

        attempts += 1
    else:
        raise RuntimeError(
            '{} consecutive sign-in attempts failed. Aborting'
            .format(max_attempts)
        )

    if two_step_detected:
        if not password:
            raise ValueError(
                "Two-step verification is enabled for this account. "
                "Please provide the 'password' argument to 'start()'."
            )
        if callable(password):
            password = password
        me = self.sign_in(phone=phone, password=password)
    signed, name = 'Signed in successfully as', utils.get_display_name(me)
    try:
        print(signed, name)
    except UnicodeEncodeError:
        print(signed, name.encode('utf-8', errors='ignore')
              .decode('ascii', errors='ignore'))
    self._check_events_pending_resolve()
    return self


if client.is_user_authorized() is not True:
    logging.info('You have not login yet, Trying to log you in... 没有活跃的登录Session，尝试登录...')
    logging.info('如果你有两步认证密码，请从官方客户端获取并输入。')
    start(client)
