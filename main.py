import logging

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CallbackQueryHandler, CommandHandler, MessageHandler, filters, InlineQueryHandler

from weather import show_tempertaure_moscow
from sport.handler import sport_news, button, help_command

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
	print('/start was called')


# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
# 	if update.message.text == 'Я тебя люблю':
# 		await context.bot.send_message(chat_id=update.effective_chat.id, text='Когда будет blowjob?')
# 	else:
# 		await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
# 	print(update.message.text)

# async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
# 	try:
# 		text_caps = ' '.join(context.args).upper()
# 		await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
# 	except:
# 		print('Забыл слова написать')
#

async def moscow_temperature(update: Update, context: ContextTypes.DEFAULT_TYPE):
	temperature = show_tempertaure_moscow()
	logging.info('Request Temperature - Moscow = ' + temperature)
	await context.bot.send_message(chat_id=update.effective_chat.id, text='На текущий момент в Москве температура равна ' + temperature)


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


if __name__ == '__main__':
	application = ApplicationBuilder().token('5918379510:AAGg8ml_tkenwI7ibDij-e5HHWJhS_5XFg4').build()

	application.add_handler(CommandHandler('start', start))
	application.add_handler(CommandHandler('sport', sport_news))
	application.add_handler(CallbackQueryHandler(button))
	application.add_handler(CommandHandler('help', help_command))
	application.add_handler(CommandHandler('weather', moscow_temperature))
	application.add_handler(MessageHandler(filters.COMMAND, unknown))

	application.run_polling()
