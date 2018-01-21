from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import os

upd = Updater(os.environ['TOKEN'])


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='welcome on board')

def help(bot, update):
    update.message.reply_text('please read the help book')

def echo(bot, update):
    txt = update.message.text
    update.message.reply_text(txt.capitalize())


upd.dispatcher.add_handler(CommandHandler('start', start))
upd.dispatcher.add_handler(CommandHandler('help', help))
upd.dispatcher.add_handler(MessageHandler(Filters.text, echo))

upd.start_polling()

upd.idle()

