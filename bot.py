import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID", "15939361"))
API_HASH = environ.get("API_HASH", "f8beb0bd0054a717d84fbe9be12a23ea")
BOT_TOKEN = environ.get("BOT_TOKEN", "5480565679:AAFHfDkrFbqB7WQ2VbYvt7orj5kPcNCejN8")
SESSION = environ.get("SESSION", "BQCHkcjTw62djL1I15Oul550oNT7xSMdDocRMoUZFYdXTuvBjnvPyz_bb-n6gBL7cKd4SU3vXf8DwyyAiItxDEBsL8A0rNsUJLVoGu6zpvliUxIudzfbFXiiAohcl-MUNo4TvK2cyOE3SOpaOHHqKDSO-xl18euExyL9p6H0XapPzrmnva9efLvLsHa5NuOi1xN8etwFeJk1VzylwWFbGgPVr2-7LY1jXR_Fyy8KwQi6UctogNJ-ltXQOu4SwMccEXGornbRJT5C05wHGxDhymQAAcTegEfjbnGI4dzMIn6zO2QpRvFUZeqqgtJs2joRpBl-ohHOaOgk8GzUDsESXBkROg1h6AA")
TIME = int(environ.get("TIME", "200"))
GROUPS = []
for grp in environ.get("GROUPS", "-1001388131154 -1001517645234 -1001743143222").split():
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
