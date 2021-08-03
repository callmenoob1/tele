from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import CallbackContext

from telegram import Update

from telegram.chataction import ChatAction

token = "1756530858:AAH0AbYk23iJ2T501o5nNLsPcl9iQQmZz24"
messages = {
    "msg_start": "سلام {} {} \n به ربات تاپلرن خوش آمدید.",
    "msg_sum": "مجموع اعداد به صورت زیر است: \n {}"
}


def start_handler(update: Update, context: CallbackContext):


    import pdb; pdb.set_trace()
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(text=messages["msg_start"].format(first_name, last_name))


def sum_handler(update: Update, context: CallbackContext):
    # return summation of input numbers.

    import pdb; pdb.set_trace()
    chat_id = update.message.chat_id
    numbers = context.args
    result = sum(int(i) for i in numbers)
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(text=messages["msg_sum"].format(result))


def main():
    updater = Updater(token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler("start", start_handler))
    updater.dispatcher.add_handler(CommandHandler("sum", sum_handler))

    updater.start_polling()

    updater.idle()


main()