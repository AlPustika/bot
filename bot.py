from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, CallbackQueryHandler
import logging
import os
import pandas as pd


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def start(bot, update):

    btn = country()
    reply_markup = InlineKeyboardMarkup(btn)
    update.message.reply_text('Select country please', reply_markup=reply_markup)



def country():
    size = 3
    df = pd.read_csv('studios.csv')  # read data
    all_cntry = pd.unique(df.Country)  # kill country with the same name
    all_cntry = sorted(all_cntry)  # sorting by alphabet
    print(all_cntry)
    rest = len(all_cntry) % size  # how many countes not in list (oatatok)
    cnt = len(all_cntry) - rest  # length for cyckling
    ls = [[InlineKeyboardButton(all_cntry[i], callback_data=all_cntry[i]),
           InlineKeyboardButton(all_cntry[i + 1], callback_data=all_cntry[i + 1]),
           InlineKeyboardButton(all_cntry[i + 2], callback_data=all_cntry[i + 2])] for i in range(0, cnt, size)]
    if rest == 1:
        ls.append([InlineKeyboardButton(all_cntry[-1], callback_data=all_cntry[-1])])#
    elif rest == 2:
        ls.append([InlineKeyboardButton(all_cntry[-1], callback_data=all_cntry[-1]),
                   InlineKeyboardButton(all_cntry[-2], callback_data=all_cntry[-2])])
    return ls

def echo(bot, update):
    txt = update.message.text
    update.message.reply_text(txt.capitalize())


def button(bot, update):
    query = update.callback_query

    bot.edit_message_text(text="Selected option: {}".format(query.data),
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)


def main():

    tok = os.environ['TOKEN']
    #print(tok)
    upd = Updater('510826842:AAGLRHUfrT4CgteJ3hzMV7HjykfrMl1EZv0')
    #print(upd)
    upd.dispatcher.add_handler(CommandHandler('start', start))
    upd.dispatcher.add_handler(CommandHandler('help', help))
    upd.dispatcher.add_handler(MessageHandler(Filters.text, echo))
    upd.dispatcher.add_handler(CallbackQueryHandler(button))
    upd.dispatcher.add_error_handler(error)
    upd.start_polling()
#################  WEBHOOK  ###############
    #upd.idle()

    #TOKEN = "TOKEN"
    #PORT = int(os.environ.get('PORT', '8443'))
    #updater = Updater(TOKEN)
    ## add handlers
    #updater.start_webhook(listen="0.0.0.0",
    #                      port=PORT,
    #                      url_path=TOKEN)
    #updater.bot.set_webhook("https://<appname>.herokuapp.com/" + TOKEN)
    #updater.idle()

if __name__== '__main__':
    main()
