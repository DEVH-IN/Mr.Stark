import os
import time
import logging
from pyrogram import Client, filters

from main.helper_func.basic_helpers import progress



@Client.on_message(filters.command(["download"]))
async def download(bot, message):
    s_time = time.time()
    await message.reply_text("Downloading to Server..")
    if not message.reply_to_message:
        await message.edit("`Reply to a message to download!")
        return
    if not message.reply_to_message.media:
        await message.edit("`Reply to a message to download!`")
        return
    c_time = time.time()
    Escobar = await message.reply_to_message.download(
        progress=progress, progress_args=(c_time, f"`Downloading This File!`")
    )
    e_time = time.time()
    dl_time = round(s_time - e_time)
    file_txt = "__Downloaded This File To__ `{}` __in__ `{}`."

    await message.edit(file_txt.format(Escobar, dl_time))