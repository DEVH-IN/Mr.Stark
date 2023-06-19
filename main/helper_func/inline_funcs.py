import aiohttp
import asyncio
import re
import sys

from pyrogram import filters
from pyrogram.raw.functions import Ping
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineQueryResultArticle,
    InlineQueryResultPhoto,
    InlineQueryResultCachedDocument,
    InputTextMessageContent,
    InlineKeyboardMarkup,
)
from Python_ARQ import ARQ
from Stark.config import Config

ARQ_URI = "http://arq.hamker.dev"
API_KEY = Config.ARQ_API
aiohttpsession = aiohttp.ClientSession()
arq = ARQ(ARQ_URI, API_KEY, aiohttpsession)


async def wall_func(answers, query):
    results = await arq.wall(query)
    if not results.ok:
        answers.append(
            InlineQueryResultArticle(
                title="Error",
                description=results.result,
                input_message_content=InputTextMessageContent(results.result),
            )
        )
        return answers
    results = results.result[:50]
    for i in results:
        answers.append(
            InlineQueryResultPhoto(
                photo_url=i.url_image,
                thumb_url=i.url_thumb,
                caption=f"[Source]({i.url_image})",
            )
        )
    return answers


async def torrent_func(answers, query):
    results = await arq.torrent(query)
    if not results.ok:
        answers.append(
            InlineQueryResultArticle(
                title="Error",
                description=results.result,
                input_message_content=InputTextMessageContent(results.result),
            )
        )
        return answers
    results = results.result[:20]
    for i in results:
        title = i.name
        size = i.size
        seeds = i.seeds
        leechs = i.leechs
        upload_date = i.uploaded
        magnet = i.magnet
        caption = f"""
**Title:** __{title}__
**Size:** __{size}__
**Seeds:** __{seeds}__
**Leechs:** __{leechs}__
**Uploaded:** __{upload_date}__
**Magnet:** `{magnet}`"""

        description = f"{size} | {upload_date} | Seeds: {seeds}"
        answers.append(
            InlineQueryResultArticle(
                title=title,
                description=description,
                input_message_content=InputTextMessageContent(
                    caption, disable_web_page_preview=True
                ),
            )
        )
    return answers


async def image_func(answers, query):
    results = await arq.image(query)
    if not results.ok:
        answers.append(
            InlineQueryResultArticle(
                title="Error",
                description=results.result,
                input_message_content=InputTextMessageContent(results.result),
            )
        )
        return answers
    results = results.result[:50]
    buttons = InlineKeyboardMarkup(row_width=2)
    buttons.add(
        InlineKeyboardButton(
            text="Search again",
            switch_inline_query_current_chat="image",
        ),
    )
    for i in results:
        answers.append(
            InlineQueryResultPhoto(
                title=i.title,
                photo_url=i.url,
                thumb_url=i.url,
                reply_markup=buttons,
            )
        )
    return answers

async def app_search(answers, query):
    app_list = search(query)
    if not app_list:
        answers.append(
            InlineQueryResultArticle(
                title="Error",
                description="Something Unexpected Error Occurred",
                input_message_content=InputTextMessageContent(
                    message_text="Something Unexpected Error Occurred"
                )
            )
        )
        return answers
    for app in app_list:
        title = app["title"]
        icon = app["icon"]
        desp = app["description"]
        rating = app["score"]
        genre = app["genre"]
        price = app["price"]
        app_id = app["appId"]
        answers.append(
            InlineQueryResultArticle(
                title=title,
                description=desp,
                input_message_content=InputTextMessageContent(
                    message_text=f"Title: {title}\n"
                                f"Description: {desp}\n"
                                f"Rating: {rating}\n"
                                f"Genre: {genre}\n"
                                f"Price: {price}\n"
                                f"App ID: {app_id}"
                ),
                thumb_url=icon
            )
        )
    return answers