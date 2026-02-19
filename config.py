import logging

from telethon import TelegramClient

from os import getenv
from AltBots.data import ALTRON


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = 18136872
API_HASH = "312d861b78efcd1b02183b2ab52a83a4"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

BOT_TOKEN = "8579272205:AAH_wAPr1Ifm-psVHdryRGESZ1k4usdzBxo"
BOT_TOKEN2 = "7959739134:AAEiizUejFlmIBQ5vdaIF8dCCfbNxPoDSJo"
BOT_TOKEN3 = "8230454751:AAH-BQTxp2C2dpeyeNJ5eIh84kK1ohT6xQg"
BOT_TOKEN4 = "8598886566:AAG3tA0fMcZ-m-uLNSq2x6Vu-mmY-QaREYQ"
BOT_TOKEN5 = "8398092926:AAGuvsl_XjojSGNAKlZHhNF7g4V8h43i_Lc"
BOT_TOKEN6 = "8511745336:AAFlNVfnE9aaCfVNNLeeZP4o2ZEGpDZPZtY"
BOT_TOKEN7 = "8398092926:AAGuvsl_XjojSGNAKlZHhNF7g4V8h43i_Lc"
BOT_TOKEN8 = "7799527731:AAFjeubTHeUGHO9mtR3s9pjJsD9Q0TmuWic"
BOT_TOKEN9 = "8578090674:AAEY-S_8kPSJZoplQBN8AHyosGqYW9eFe6U"
BOT_TOKEN10 = "8493913384:AAGXkW4_UmePp07Jc-_chC5bZtSuXvS75uk"

SUDO_USERS = list(map(lambda x: int(x), "1157931747".split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int("1157931747")
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
X2 = TelegramClient('X2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
X3 = TelegramClient('X3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
X4 = TelegramClient('X4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
X5 = TelegramClient('X5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
X6 = TelegramClient('X6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
X7 = TelegramClient('X7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
X8 = TelegramClient('X8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
X9 = TelegramClient('X9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
X10 = TelegramClient('X10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
