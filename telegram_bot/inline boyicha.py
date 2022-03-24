from telegram.ext import Updater, MessageHandler, CommandHandler, ConversationHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup


def start(update, context):
    update.message.reply_text("Yetkazib berish bo'limi Toshkent shaxrida soat 10:00 dan 3:00 gacha ishlaydi.")
    update.message.reply_text("Buyurtmani birga joylashtiramizmi? 🤗")

def main():
    token = "5234074523:AAEeKOvtz_5jZFJelEhc_ZhU3YVYLdtvBcU"
    updater = Updater(token)

    updater.dispatcher.add_handler(CommandHandler("start", start))


    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()








