from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove
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

    update.message.reply_text('Select country or job position', reply_markup=ReplyKeyboardMarkup([['Country', 'Job Position']], resize_keyboard=True,one_time_keyboard=True))


def country():
    size = 3
    df = pd.read_csv('studios.csv')  # read data
    all_cntry = pd.unique(df.Country)  # kill country with the same name
    all_cntry = sorted(all_cntry)  # sorting by alphabet
    #print(all_cntry)
    rest = len(all_cntry) % size  # how many countes not in list (ostatok)
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


def city(cntry):
    size = 3
    df = pd.read_csv('studios.csv')  # read data
    all_city = pd.unique(df[df.Country == cntry][['City']].squeeze())
    all_city = sorted(all_city)  # sorting by alphabet
    #print(all_city)
    rest = len(all_city) % size  # how many countes not in list (ostatok)
    cnt = len(all_city) - rest  # length for cyckling
    ls = [[InlineKeyboardButton(all_city[i], callback_data=all_city[i]),
           InlineKeyboardButton(all_city[i + 1], callback_data=all_city[i + 1]),
           InlineKeyboardButton(all_city[i + 2], callback_data=all_city[i + 2])] for i in range(0, cnt, size)]
    if rest == 1:
        ls.append([InlineKeyboardButton(all_city[-1], callback_data=all_city[-1])])#
    elif rest == 2:
        ls.append([InlineKeyboardButton(all_city[-1], callback_data=all_city[-1]),
                   InlineKeyboardButton(all_city[-2], callback_data=all_city[-2])])

    return ls


def echo(bot, update):
    txt = update.message.text
    update.message.reply_text('good buy', reply_markup=ReplyKeyboardRemove())
    #print(update.callback_query)
    if txt == 'Country':
        btn = country()
        reply_markup = InlineKeyboardMarkup(btn)
        update.message.reply_text('Select country please', reply_markup=reply_markup)
        #city = pd.unique(df[df.Country == cnt][['City']].squeeze())


def button(bot, update):
    query = update.callback_query
    bot.edit_message_text(text="Selected option: {}".format(query.data),
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)
    print(query.data)
    cities = city(query.data)
    if cities:
       # print(cities)
        reply_markup2 = InlineKeyboardMarkup(cities)
       #update.message.reply_text('Cities for selected Country:', reply_markup=reply_markup2)
    keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
                 InlineKeyboardButton("Option 2", callback_data='2')],

                [InlineKeyboardButton("Option 3", callback_data='3')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
#
    #bot.edit_message_text('Please choose:')
    #bot.sendMessage(chat_id=update.message.chat_id, text='hallo')
    print('bot', bot)
    print('update', update)

def main():

    tok = os.environ['TOKEN']
    #print(tok)
    upd = Updater('492259029:AAEY4oqW4rGVNRLJdZx-Yt1UOyNN6e2SB-U')
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
