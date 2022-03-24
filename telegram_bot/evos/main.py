import ast
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from services import *

log = {"state": 0}

cont = ReplyKeyboardMarkup([[KeyboardButton("Contact", request_contact=True)]], resize_keyboard=True)




def key_btns(type=None, ctg=None):
    btn = []
    if type == "menu":
        ctgs = get_kategiriya()
        for i in range(1, len(ctgs), 2):
            btn.append([
                KeyboardButton(ctgs[i-1][1]),
                KeyboardButton(ctgs[i][1]),
            ])


        if len(ctgs) % 2:
            btn.append([KeyboardButton(ctgs[-1][1])])

        btn.append([
            KeyboardButton("📥 Savat"), KeyboardButton("⬅️ Ortga")
        ])
    elif type == "ctg":
        prod = get_product(ctg=ctg)
        for i in range(1, len(prod), 2):
            btn.append([
                KeyboardButton(prod[i-1][1]),
                KeyboardButton(prod[i][1]),
            ])


        if len(prod) % 2:
            btn.append([KeyboardButton(prod[-1][1])])

        btn.append([
            KeyboardButton("⬅️ Ortga")
        ])

    elif type == "number":
        for i in range(1, 10, 3):
            btn.append([
                InlineKeyboardButton(f"{i}", callback_data=f'{i}'),
                InlineKeyboardButton(f'{i+1}', callback_data=f'{i+1}'),
                InlineKeyboardButton(f'{i+2}', callback_data=f'{i+2}'),
            ])

        btn.append([InlineKeyboardButton("⬅️ Ortga", callback_data="back")])

        return InlineKeyboardMarkup(btn)
    else:
        btn = [
            [KeyboardButton("🍴 Menu")],
            [KeyboardButton("🛍 Mening buyurtmalarim")],
            [KeyboardButton("✍️ Fikr bildirish"), KeyboardButton("⚙️ Sozlamalar")]
        ]

    return ReplyKeyboardMarkup(btn, resize_keyboard=True)

def start(update, context):
    user = update.message.from_user
    log = get_log(user.id)
    if log is None:
        log = create_log(user.id)
    log = ast.literal_eval(log[1]) #dictionary ga o`qazish
    log['state'] = 1

    tg_user = get_user(user.id)
    if tg_user is not None:
        log['state'] = 4
        clear_log(user.id, 4)
        update.message.reply_text("Menulardan birini tanlang👇", reply_markup=key_btns())
        return

    update.message.reply_text("Assalomu aleykum.\nIsmingizni kirirting👇 ")


    change_log(user.id, log)

def recieved_msg(update, context):
    user = update.message.from_user
    log = get_log(user.id)
    log = ast.literal_eval(log[1])

    msg = update.message.text
    state = log.get('state', 0)


    if msg == "🍴 Menu":
        log["state"] = 5
        update.message.reply_text("Bo'limni tanlang.", reply_markup=key_btns("menu"))


    if state == 1:
        log["ism"] = msg
        log["state"] = 2
        update.message.reply_text("Iltimos Familiyangizni kiriting👇")
    elif state == 2:
        log['familiya'] = msg
        log["state"] = 3
        update.message.reply_text(f"Raqamingizni kiriting👇", reply_markup=cont)


    elif state == 5:
        if msg == "⬅️ Ortga":
            log['state'] = 4
            clear_log(user.id, 4)
            update.message.reply_text("Menulardan birini tanlang👇", reply_markup=key_btns())
        else:
            log['state'] = 6
            update.message.reply_text("Quyidagi mahsulotlardan birini tanlang👇", reply_markup=key_btns("ctg", ctg=msg))


    elif state == 6:
        if msg == "⬅️ Ortga":
            log['state'] = 5
#            update.message.reply_text("Menulardan birini tanlang👇", reply_markup=key_btns("menu"))
            update.message.reply_text("Bo'limni tanlang.👇", reply_markup=key_btns("menu"))
        else:
            log["state"] = 6
            product = get_product(nomi=msg)
            context.bot.send_photo(photo=open(product[5], 'rb'),
                                   caption=f"{product[2]}, \nNarxi: {product[3]}",
                                    chat_id=user.id,
                                   reply_markup=key_btns(type="number")
                                    )


    change_log(user.id, log)

def contact_handler(update, context):
    user = update.message.from_user
    log = get_log(user.id)
    log = ast.literal_eval(log[1])
    contact = update.message.contact
    state = log.get('state', 0)
    print(contact)

    if state == 3:
        log['state'] = 4
        log['raqam'] = contact.phone_number
        add_user(user.id, log)
        clear_log(user.id, 4)
        update.message.reply_text("Menulardan birini tanlang👇", reply_markup=key_btns())

#contact ushlab olish

#    change_log(user.id, log)

def main():
    updater = Updater("5234074523:AAEeKOvtz_5jZFJelEhc_ZhU3YVYLdtvBcU")
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, recieved_msg))
    updater.dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))


    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
