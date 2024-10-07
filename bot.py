import telebot

# توكن البوت مالك
TOKEN = "7465740739:AAGy4E81py1JUMOzcntalDk7dqHG4_LPPrU"

# إنشاء البوت باستخدام التوكن
bot = telebot.TeleBot(TOKEN)

# دالة تستلم الرسائل
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلًا! شلونك؟ هذا بوت تجريبي!")

# دالة تستلم أي رسالة نصية وترجعها
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

# تشغيل البوت باستخدام polling
bot.infinity_polling()
