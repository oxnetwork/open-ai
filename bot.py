import telegram
import openai

# متصل شدن به API OpenAI
openai.api_key = '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'

# ایجاد یک بات جدید تلگرام
bot = telegram.Bot(token='6091612211:AAFdtOg0--Wt3_TMkv0Hqhtflc4eVRFoxyM')

# تعریف دستور /start
def start(update, context):
    message = "سلام! به ربات تلگرام ChatGPT خوش آمدید."
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# تعریف دستور /echo
def echo(update, context):
    message = update.message.text
    response = openai.Completion.create(engine="text-davinci-002", prompt=message, max_tokens=1024)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)

# تعریف هندلر برای دستورها
from telegram.ext import CommandHandler, MessageHandler, Filters
start_handler = CommandHandler('start', start)
echo_handler =
