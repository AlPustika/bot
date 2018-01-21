from telegram.ext import Updater, CommandHandler

token = '539369144:AAFPK7WUyI0t0wQPfOKRdlgAmhQRWf_Y4-M'
upd = Updater(token)


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='welcome on board')

def help(bot, update):
    update.message.reply_text('please read the help book')


upd.dispatcher.add_handler(CommandHandler('start', start))
upd.dispatcher.add_handler(CommandHandler('help', help))

upd.start_polling()

upd.idle()

