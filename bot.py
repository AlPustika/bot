from telegram.ext import Updater, CommandHandler

token = '539369144:AAFPK7WUyI0t0wQPfOKRdlgAmhQRWf_Y4-M'
upd = Updater(token)


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='welcome on board')


upd.dispatcher.add_handler(CommandHandler('start', start))

upd.start_polling()

upd.idle()

