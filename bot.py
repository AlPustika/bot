from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, CallbackQueryHandler

import os

upd = Updater(os.environ['TOKEN'])


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='welcome on board')

def help(bot, update):
    update.message.reply_text('you have been warned')

def echo(bot, update):
    txt = update.message.text
    update.message.reply_text(txt.capitalize())

def main():
    upd.dispatcher.add_handler(CommandHandler('start', start))
    upd.dispatcher.add_handler(CommandHandler('help', help))
    upd.dispatcher.add_handler(MessageHandler(Filters.text, echo))

    upd.start_polling()

    #upd.idle()


if __name__== '__main__':
    main()