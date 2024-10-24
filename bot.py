import telebot
#لا تحاول يا غشاش 🤣
TOKEN = "token"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def se(message):
    bot.reply_to(message, "أكوتشي لوتشي موتشي 😂")
bot.infinity_polling()
