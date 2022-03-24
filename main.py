from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

import aiocron

from configparser import ConfigParser
from datetime import datetime
from pytz import timezone

import string
import random


# Config
conf = ConfigParser()
conf.read('./config.ini')

api_id = int(conf.get('account', 'api_id'))
api_hash = conf.get('account', 'api_hash')
phone_number = conf.get('account', 'phone_number')

client = TelegramClient('session', api_id, api_hash)
client.start(phone=phone_number)

TIMEZONE = conf.get('time', 'timezone')
FONTS = [
    ["𝟬", "𝟭", "𝟮", "𝟯", "𝟰", "𝟱", "𝟲", "𝟳", "𝟴", "𝟵"],
    ["𝟘", "𝟙", "𝟚", "𝟛", "𝟜", "𝟝", "𝟞", "𝟟", "𝟠", "𝟡"],
    ["₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉"],
]


# Crontab
@aiocron.crontab('*/1 * * * *')
async def update_profile():
    now = datetime.now(timezone(TIMEZONE))
    table = str.maketrans(string.digits, ''.join(random.choice(FONTS)))
    time = now.strftime("%H:%M").translate(table)
    await client(UpdateProfileRequest(last_name=time))


if __name__ == '__main__':
    client.loop.run_until_complete(client.run_until_disconnected())

