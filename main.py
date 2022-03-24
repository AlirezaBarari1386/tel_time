from datetime import datetime
from random import choice

from aiocron import crontab
from pyrogram import Client, idle
from pytz import timezone

api_id = 0
api_hash = ""

phone_number = ""

time_zone = timezone("Asia/Tehran")

fonts = [
    ["𝟬", "𝟭", "𝟮", "𝟯", "𝟰", "𝟱", "𝟲", "𝟳", "𝟴", "𝟵"],
    ["𝟘", "𝟙", "𝟚", "𝟛", "𝟜", "𝟝", "𝟞", "𝟟", "𝟠", "𝟡"],
    ["₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉"],
]

app = Client(
    "bot",
    api_id,
    api_hash,
    phone_number=phone_number,
)


@crontab("*/1 * * * *", tz=time_zone, start=False)
async def change_name():
    table = str.maketrans("0123456789", "".join(choice(fonts)))
    time = datetime.now(time_zone).strftime("%H:%M")
    await app.update_profile(last_name=time.translate(table))


if __name__ == "__main__":
    app.start()
    change_name.start()
    idle()
    change_name.stop()
    app.stop()