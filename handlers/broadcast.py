from pyrogram import Client, filters
from pyrogram.types import Message
from helpers.filters import command
from helpers.database import db
from helpers.dbtools import main_broadcast_handler
from config import (
    BOT_USERNAME,
    SUDO_USERS,
)
@Client.on_message(
    filters.private
    & filters.command("broadcast")
    & filters.user(SUDO_USERS)
    & filters.reply
)
async def broadcast_handler_open(_, m: Message):
    await main_broadcast_handler(m, db)
