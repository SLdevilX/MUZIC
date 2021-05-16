# © lasiya
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
import youtube_dl
from youtube_search import YoutubeSearch
import requests

import os
from config import Config

bot = Client(
    'MissRose',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)



## Commands --------------------------------

@bot.on_message(filters.command(['start']))
def start(client, message):
    Sldevilx = f'╭─━━━━━━━━━━━━━━━━━─╮\n\n       🤟 Hey @{message.from_user.username} [😏🎧](https://telegra.ph/file/534ba62f07c64c5fb25ef.jpg)\n      Welcome to X-Troid MUZIC \n To use me Type with this format👇 \n           /song song name\n\n╰─━━━━━━━━━━━━━━━━━─╯'
    message.reply_text(
        text=Sldevilx, 
        quote=False,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Owner🎸', url='http://t.me/Danuma_admin_bot'),
                    InlineKeyboardButton('About Owner💡', url='https://lasiya.ml'),
                ],
                [
                    InlineKeyboardButton('Main Group 🇱🇰', url='http://t.me/Danuma01')
                ],
                [
                    InlineKeyboardButton('Bot Channel 🏅', url='http://t.me/danumabots')
                 ]
            ]
            
        )
    )

bot.run()
