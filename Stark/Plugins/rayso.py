#Credits to CatUB
#Originally made in telethon ny @feelded
#Ported to Pyrogram by @Naveen_xD

import os
import random
from Stark import error_handler
from pyrogram import Client, filters
from main.helper_func.google_chrome import chromeDriver

THEMES = [
    "breeze",
    "candy",
    "crimson",
    "falcon",
    "meadow",
    "midnight",
    "raindrop",
    "sunset",
]

MODES = ["mode-day", "mode-night"]


def text_chunk_list(query, bits=29900):
    text_list = []
    string = query
    checker = len(query)
    if checker > bits:
        limit = int(checker / (int(checker / bits) + 1))
        string = ""

        for item in query.split(" "):
            string += f"{item} "
            if len(string) > limit:
                string = string.replace(item, "")
                text_list.append(string)
                string = ""
    if string != "":
        text_list.append(string)
    return text_list


@Client.on_message(filters.command("rayso"))
@error_handler
async def rayso_by_pro_odi(c, m):
    "To paste text or file into image."
    files = []
    captions = []
    try:
      query = m.text.split(None, 1)[1]
    except IndexError:
      query = None
    if m.reply_to_message:
      rquery = m.reply_to_message
    else:
      rquery = None
    rayso = await m.reply_text("**Processing...**")
    if not query:
      theme = "random"
    if query and (query.lower() in THEMES):
      theme = query
    if query and (query.lower() not in THEMES) and (query != "-l"):
      await rayso.edit("`Invalid Theme selected")
      return
    # Themes List
    if query == "-l":
        ALLTHEME = "**🎈Modes:**\n**1.**  `Mode-Day`\n**2.**  `Mode-Night`\n\n**🎈Themes:**\n**1.**  `Random`"
        for i, each in enumerate(THEMES, start=2):
            ALLTHEME += f"\n**{i}.**  `{each.title()}`"
        return await rayso.edit(ALLTHEME)

    # Get Theme
    if theme == "random":
        theme = random.choice(THEMES)

    # Get Mode
    if rquery:
        if rquery.text:
            text = rquery.text
        elif rquery.caption:
            text = rquery.caption
        else:
            return await rayso.edit("`Unsupported.`")
    else:
        return await rayso.edit("`What should I do?`")

    # // Max size 30000 byte but that breaks thumb so making on 28000 byte
    text_list = text_chunk_list(text, 28000)
    user = m.from_user.first_name
    for i, text in enumerate(text_list, start=1):
        await rayso.edit(f"`Making Rayso Image: {i}/{len(text_list)} `")
        outfile, error = chromeDriver.get_rayso(
            text, darkMode=True, file_name=f"rayso{i}.png", title=user, theme=theme
        )
        if error:
            return await rayso.edit(error)
        files.append(outfile)
        captions.append("")

    await rayso.edit("**__Uploading...__**")
    captions[-1] = f"<i>➥ Generated by : <b>{m.from_user.mention}</b></i>"
    for i in files:
        await c.send_document(
          m.chat.id,
          i,
          caption=captions,
      )
    await rayso.delete()
    for name in files:
        os.remove(name)

@Client.on_message(filters.command(["lrayso", "light_rayso"]))
@error_handler
async def light_mode_rayso(c, m):
    files = []
    captions = []
    try:
      query = m.text.split(None, 1)[1]
    except IndexError:
      query = None
    if m.reply_to_message:
      rquery = m.reply_to_message
    else:
      rquery = None
    rayso = await m.reply_text("**Processing...**")
    if not query:
      theme = "random"
    if query and (query.lower() in THEMES):
      theme = query
    if query and (query.lower() not in THEMES) and (query != "-l"):
      await rayso.edit("`Invalid Theme selected")
      return
    # Themes List
    if query == "-l":
        ALLTHEME = "**🎈Modes:**\n**1.**  `Mode-Day`\n**2.**  `Mode-Night`\n\n**🎈Themes:**\n**1.**  `Random`"
        for i, each in enumerate(THEMES, start=2):
            ALLTHEME += f"\n**{i}.**  `{each.title()}`"
        return await rayso.edit(ALLTHEME)

    # Get Theme
    if theme == "random":
        theme = random.choice(THEMES)

    # Get Mode
    if rquery:
        if rquery.text:
            text = rquery.text
        elif rquery.caption:
            text = rquery.caption
        else:
            return await rayso.edit("`Unsupported.`")
    else:
        return await rayso.edit("`What should I do?`")

    # // Max size 30000 byte but that breaks thumb so making on 28000 byte
    text_list = text_chunk_list(text, 28000)
    user = m.from_user.first_name
    for i, text in enumerate(text_list, start=1):
        await rayso.edit(f"`Making Rayso Image: {i}/{len(text_list)} `")
        outfile, error = chromeDriver.get_rayso(
            text, darkMode=false, file_name=f"rayso{i}.png", title=user, theme=theme
        )
        if error:
            return await rayso.edit(error)
        files.append(outfile)
        captions.append("")

    await rayso.edit("**__Uploading...__**")
    captions[-1] = f"<i>➥ Generated by : <b>{m.from_user.mention}</b></i>"
    for i in files:
        await c.send_document(
          m.chat.id,
          i,
          caption=captions,
      )
    await rayso.delete()
    for name in files:
        os.remove(name)