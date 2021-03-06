# Copyright (C) 2020-2021 by AnossaTG@Github, < https://github.com/AnossaTG >.
#
# This file is part of < https://github.com/AnossaTG/ElectronUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/AnossaTG/ElectronUserBot/blob/master/LICENSE >
#
# All rights reserved.

from database import db_x

gbun = db_x["GBAN"]


async def gban_user(user, reason="#GBan gerçekleşti"):
    await gbun.insert_one({"user": user, "reason": reason})


async def ungban_user(user):
    await gbun.delete_one({"user": user})


async def gban_list():
    return [lo async for lo in gbun.find({})]


async def gban_info(user):
    kk = await gbun.find_one({"user": user})
    if not kk:
        return False
    else:
        return kk["reason"]
