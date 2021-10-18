import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")
load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Camila Music")
BOT_USERNAME = getenv("BOT_NAME", "TotoMusicBot")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ELECTROBOT_SUPPORT")
UPDATES_CHANNEL = getenv("BOT_NAME", "electro_updates")
BROADCAST_AS_COPY = getenv("BROADCAST_AS_COPY", "False")
LOG_CHANNEL = getenv("LOG_CHANNEL", "-1001193972853")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
DATABASE_URL = os.environ.get("DATABASE_URL") # fill with your mongodb url
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
