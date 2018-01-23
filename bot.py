from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, CallbackQueryHandler
import logging
import os
import pandas as pd

upd = Updater(os.environ['TOKEN'])
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def start(bot, update):
    cntr=['Country1','Country2','Country3''Country4']
    #btn = [[InlineKeyboardButton('Country1', callback_data='Country1'),
    #        InlineKeyboardButton('Country2', callback_data='Country2'),
    #        InlineKeyboardButton('Country3', callback_data='Country3'),
    #        InlineKeyboardButton('Country4', callback_data='Country4')]]
    #btn = [[InlineKeyboardButton('Country' + str(i), callback_data='Country' + str(i)) for i in range(1,5)]]
    #cn = ['England', 'France', 'Spain', 'Belgium', 'Poland', 'Germany', 'Finland', 'Pakistan', 'India', 'Netherlands']
    df = pd.read_csv('studios.csv')

    cn = pd.unique(df.Country)

    btn = [[InlineKeyboardButton(cn[i], callback_data=cn[i]),
           InlineKeyboardButton(cn[i + 1], callback_data=cn[i + 1]),
           InlineKeyboardButton(cn[i + 2], callback_data=cn[i + 2])] for i in range(0, len(cn)-2, 3)]

    print (btn)#
    reply_markup = InlineKeyboardMarkup(btn)
    update.message.reply_text('Command: /buttons', reply_markup= reply_markup)


def help(bot, update):
    update.message.reply_text('you have been iop')


def echo(bot, update):
    txt = update.message.text
    update.message.reply_text(txt.capitalize())


def button(bot, update):
    query = update.callback_query

    bot.edit_message_text(text="Selected option: {}".format(query.data),
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)


def main():
    upd.dispatcher.add_handler(CommandHandler('start', start))
    upd.dispatcher.add_handler(CommandHandler('help', help))
    upd.dispatcher.add_handler(MessageHandler(Filters.text, echo))
    upd.dispatcher.add_handler(CallbackQueryHandler(button))
    upd.dispatcher.add_error_handler(error)
    upd.start_polling()

    #upd.idle()


if __name__== '__main__':
    main()

#l = range(1, 10)
#print ([l[x:x+10] for #x in range(0, len(l), 1)])