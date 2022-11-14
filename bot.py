import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID", "15939361"))
API_HASH = environ.get("API_HASH", "f8beb0bd0054a717d84fbe9be12a23ea")
BOT_TOKEN = environ.get("BOT_TOKEN", "5480565679:AAFHfDkrFbqB7WQ2VbYvt7orj5kPcNCejN8")
SESSION = environ.get("SESSION", "BQAm9A0N3MQMs42zER-1amPJVszw_CPcPOH9zoV6NYZdblkb2NEWnrA6iRxXUu4qrRqwKxCHjJ1Nz3GRs5R7lEYyM8D6FZClw654BtQo3PMpBxXToSsmAz3kJ_5308dv6I045irdd63zr5arK5OUyvPJWomICXaLhiuontNEVBTFXK2lOsh-4Cz3ebXPFFqXROZIhGIosmqF7bVz0MoB0mf2Pt1_N55Yw1x7ADBf7x80Tl-al0l01U54DppXmf3BMbI719BbBZ-Mfycsu3xzmjVzflz3mN57iX_LXydxRAFAVZFE9iBrRwpjLOHMPac4k0ij3VAXqWsx9oTak4eD6yUrOg1h6AA")
TIME = int(environ.get("TIME", "200"))
GROUPS = []
for grp in environ.get("GROUPS", "-1001388131154 -1001517645234").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get("ADMINS", "5543917190").split():
    ADMINS.append(int(usr))

START_MSG = "<b>Hai {},\nI'm a private bot of @Am_Robots to delete group messages after a specific time</b>"


User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )


Bot = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.id)
    except Exception as e:
       print(e)
       
User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
