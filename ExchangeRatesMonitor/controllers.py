from telebot import types
from telebot.async_telebot import AsyncTeleBot


async def get_rates_handler(message: types.Message, bot: AsyncTeleBot):
    await bot.send_message(message.chat.id, 'pls use /joke')

def register_handlers(bot: AsyncTeleBot):
    bot.register_(
        get_rates_handler,
        func=lambda message: message.text == '/joke',
        pass_bot=True)
