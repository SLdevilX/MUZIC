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

    
 @bot.on_message(filters.command(['help']))
def help(client, message):
    Lasi = f'Respect to Dev & Give credits When you edit it,\n Dont foget to Give STAR to Original Repo.'
    message.reply_text(
        text= Lasi, 
        quote=False,
        reply_markup=InlineKeyboardMarkup(
            [
                 [
                  InlineKeyboardButton('Souce code', url='https://github.com/SLdevilX/MUZIC'),
                   InlineKeyboardButton('Howto Deploy💡', url='https://lasiya.ml'),
                ]
            ]
        )
    )


    

bot.run()
