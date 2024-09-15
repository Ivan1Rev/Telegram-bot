import requests
from typing import Final
from telegram import ForceReply, Update
import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import json

#TOKEN: Final = '7057166888:AAEe2PAsYv9t4mvQQ2P1BVTmB5L19NCJffc'
#BOT_USERNAME: Final = '@Luckzelx_weather_bot'

'''

response = requests.get('https://api2.icodrops.com/portfolio/api/markets/competitors/bitcoin')
r = response.json()
print(r)
print("USD price compared to 1 bitcoin is:", r["marketCompetitors"][0]['price']['USD'])
'''




# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! I am a weather bot, please use /help for further information.",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    user = update.effective_user
    await update.message.reply_html(f"Hello {user.mention_html()} please write /weather ... "
                                                                     "(followed by the country you want the weather "
                                                                     "information on), example: /weather Spain")

    #await update.message.reply_text(f"Hello my {user.reply_text()}")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    user = update.effective_user
    await update.message.reply_text("Please use /help for further information.")


#await update.message.reply_text("Hello, I am a weather bot, please write  /weather [country]  to get the current weather in that country.")

async def weather (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    #await update.message.reply_text("Hello, I am a weather bot, please write  /weather [country]  to get the current weather in that country.")
    response = requests.get(f'https://api.weatherapi.com/v1/current.json?q={update.message.text}&key=b91c18c86cae4550924124859242804')
    r = response.json()
    current = r["current"]['temp_c']



    #print(current)
    await update.message.reply_text (f''
                                     f'The temprature in {r["location"]["tz_id"]} is {current} degrees celcuis, '
                                     f'feels like {r["current"]["feelslike_c"]} degrees celcuis.'
                                     f'Its {r["current"]["condition"]["text"]} and {r["current"]["humidity"]}% humid.'
                                     f''
                                     )


#"humidity"feelslike_c",condition"text"
def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("7057166888:AAEe2PAsYv9t4mvQQ2P1BVTmB5L19NCJffc").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("Weather", weather))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()


'''
country = input("What country are you from?")
response = requests.get(f'https://api.weatherapi.com/v1/current.json?q={country}&key=b91c18c86cae4550924124859242804')
r = response.json()
print("In", r['location']['name'], "the temprature is ", r['current']['temp_c'], "Celsius")
'''

#print(response.json())
#7057166888:AAEe2PAsYv9t4mvQQ2P1BVTmB5L19NCJffc
#https://www.youtube.com/watch?v=vZtm1wuA2yc
#https://docs.python-telegram-bot.org/en/stable/examples.echobot.html