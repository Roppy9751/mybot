from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler) # Command Handler (/start , /finish ...)
import logging
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level = logging.INFO,
					filename = 'bot.log'
	)


def great_user(bot ,update):
	text = 'Fuuuu'
	logging.info(text)
	update.message.reply_text("yeahboy")


def talk_to_me(bot , update):
	user_text = update.message.text
	print(user_text)
	update.message.reply_text(user_text)



#This is the body of our telegram bot 

def body():
	mybot = Updater(setting.API_Key)


	dp =mybot.dispatcher
	dp.add_handler(CommandHandler("start" , great_user ))
	dp.add_handler(MessageHandler(Filters.text , talk_to_me))
	mybot.start_polling()
	mybot.idle()

body()

