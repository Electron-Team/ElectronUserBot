# Copyright (C) 2020-2021 by AnossaTG@Github, < https://github.com/AnossaTG >.
#
# This file is part of < https://github.com/AnossaTG/ElectronUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/AnossaTG/ElectronUserBot/blob/master/LICENSE >
#
# All rights reserved.

from database import db_x

nsfw = db_x["NSFW_WATCH"]


async def add_chat(chat_id):
    await nsfw.insert_one({"chat_id": chat_id})


async def rm_chat(chat_id):
    await nsfw.delete_one({"chat_id": chat_id})


async def get_all_nsfw_chats():
    return [kek async for kek in nsfw.find({})]


async def is_chat_in_db(chat_id):
    k = await nsfw.find_one({"chat_id": chat_id})
    return bool(k)
