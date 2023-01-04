from telebot.async_telebot import AsyncTeleBot
from telebot.types import BotCommand

import yaml
from yaml.loader import SafeLoader

with open("settings.yml", 'r') as stream:
    settings = yaml.load(stream, SafeLoader)
    bot_token = settings['token']
    links = settings['bank rates links']

bot = AsyncTeleBot(bot_token)
bot.set_my_commands([
	BotCommand('/start', 'main menu')
])
