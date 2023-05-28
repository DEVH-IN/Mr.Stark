import os
import requests 
from imdb import IMDb
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Stark import error_handler

ia = IMDb()

@Client.on_message(filters.command(["imdb", "IMDb"]))
@error_handler
async def search_movie(bot, message):
    if len(message.command) < 2:
        await message.reply_text("Please provide a movie or TV series name after the /imdb command.")
        return

    query = " ".join(message.command[1:])
    movies = ia.search_movie(query)
    if movies:
        movie = movies[0]
        ia.update(movie, ["main", "plot", "cast", "cover url", "language", "countries", "plot outline"])

        title = movie["title"]
        year = movie["year"]
        rating = movie["rating"]
        plot = movie["plot"][0]
        genres = ", ".join(movie["genres"])
        director = movie["director"][0]["name"]
        cast = ", ".join([actor["name"] for actor in movie["cast"][:5]])
        runtime = movie["runtimes"][0]
        language = movie["language"][0]
        countries = ", ".join(movie["countries"])
        plot_outline = movie.get("plot outline", "")
        cover_url = movie.get("cover url", "")

        caption = f"🎬 Title: {title}\n"
        caption += f"⭐️ Rating: {rating}\n"
        caption += f"🔍 Plot: {plot}\n"
        caption += f"📅 Year: {year}\n"
        caption += f"🌟 Genres: {genres}\n"
        caption += f"🎬 Director: {director}\n"
        caption += f"🌐 Language: {language}\n"
        caption += f"🌍 Countries: {countries}\n"
        caption += f"⏱️ Runtime: {runtime} mins\n"

        poster_path = f"poster_{movie.movieID}.jpg"
        response = requests.get(cover_url)
        with open(poster_path, "wb") as file:
            file.write(response.content)

        await bot.send_photo(
            chat_id=message.chat.id,
            photo=poster_path,
            caption=caption,
            reply_markup=get_inline_keyboard(movie.movieID)
        )
        os.remove(poster_path)
    else:
        await message.reply_text("No movie found.")

def generate_movie_caption(movie):
    title = movie["title"]
    year = movie["year"]
    rating = movie["rating"]
    plot = movie["plot"][0]
    genres = ", ".join(movie["genres"])
    director = movie["director"][0]["name"]
    cast = ", ".join([actor["name"] for actor in movie["cast"][:5]])
    runtime = movie["runtimes"][0]
    language = movie["language"][0]
    countries = ", ".join(movie["countries"])
    plot_outline = movie.get("plot outline", "")
    cover_url = movie.get("cover url", "")

    caption = f"🎬 Title: {title}\n"
    caption += f"⭐️ Rating: {rating}\n"
    caption += f"🔍 Plot: {plot}\n"
    caption += f"📅 Year: {year}\n"
    caption += f"🌟 Genres: {genres}\n"
    caption += f"🎬 Director: {director}\n"
    caption += f"🌐 Language: {language}\n"
    caption += f"🌍 Countries: {countries}\n"
    caption += f"⏱️ Runtime: {runtime} mins\n"

    return generate_movie_caption


def get_inline_keyboard(movie):
    keyboard = []
    streaming_sites_button = InlineKeyboardButton(
        text="Streaming Sites",
        callback_data=f"streaming_sites_{movie}"
    )
    keyboard.append([streaming_sites_button])
    return InlineKeyboardMarkup(keyboard)