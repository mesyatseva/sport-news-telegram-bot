from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from sport.sport import sports_ru_football, sports_ru_hockey


async def sport_news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	keyboard = [
			[InlineKeyboardButton("Last Football News", callback_data="football")],
			[InlineKeyboardButton("Last Hockey News", callback_data="hockey")]
			]

	reply_markup = InlineKeyboardMarkup(keyboard)
	await update.message.reply_text('Please choose: ', reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	query = update.callback_query
	news = None
	if query.data == 'football':
		news = sports_ru_football()
	elif query.data == 'hockey':
		news = sports_ru_hockey()
	if news is None:
		await context.bot.send_message(chat_id=update.effective_chat.id,
									   text='Здесь случилась ошибка со стороны рудого, простите его нуба')
	else:
		message_text = ''
		number = 1
		for key in news:
			message_text += "{0}. {1} ({2})".format(number, key, news[key])
			message_text += '\n\n'
			number += 1
		await context.bot.send_message(chat_id=update.effective_chat.id, text=message_text)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	"""Displays info on how to use the bot."""
	await update.message.reply_text("Use /sport to test this bot.")
