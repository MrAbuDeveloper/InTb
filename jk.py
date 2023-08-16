from telebot import TeleBot
from telebot.types import Message

TOKEN = "6488928366:AAGZqUTNSiHtjLAgoE3LbTxmMHVKtv6U9bc"

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message: Message):
    print(message)
    chat_id =message.chat.id
    first_name = message.from_user.first_name
    bot.send_message(chat_id, f"Hello {first_name}✋✋✋. How are you doing today")

@bot.message_handler(content_types=["text"])
def Giant(message: Message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    bot.send_message(chat_id, f"Assalomu alaykum {first_name}✋✋✋. Bugun o'zingizni yaxshi his qilayabsizmi")


bot.polling()


