from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup

btn = [
    [KeyboardButton("USD"), KeyboardButton("RUB")],
    [KeyboardButton("CYN"), KeyboardButton("EUR")],
    [KeyboardButton("CAD"), KeyboardButton("GBP")]
]


def start(update, context):
    user = update.message.from_user
    update.message.reply_text(f"Assalomu aleykum{user.first_name}", reply_markup=ReplyKeyboardMarkup(btn,
                                                                                                     resize_keyboard=True))
#Assalomu aleykum deb foydalanuvchini user name chiqadi


def info(update, context):
    user = update.message.from_user
    s = f"User_id: {user.id}\nIsm: {user.first_name}\nfamiliya: {user.last_name}\nFoydalanuvchi Nomi:{user.username}"
    update.message.reply_text(s)
#foydalanuvchini malumotlari chiqadi.


def message_handler(update, context):
    msg = update.message.text
    if msg == "salom":
        update.message.reply_text("Assalomu aleykum")
    else:
        update.message.reply_text("bizda hozircha faqat salom bor)")
#foydalanuvchi nimani yozgan bolsa shuni chiqaradi.



def image_handler(update, context):
    img = update.message.photo
    print(img)
#rasmni yuklab olish va uni ushlash



def loc(update, context):
    loc = update.message.location
    print(loc)
#locatsiya olish



def main():
    TOKEN = "5234074523:AAEeKOvtz_5jZFJelEhc_ZhU3YVYLdtvBcU"
    updater = Updater(TOKEN)
#telegram botimizning TOKEN FAYLI


    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("info", info))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.photo, image_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.location, loc))

    updater.start_polling()
    updater.idle()



if __name__ == "__main__":
    main()