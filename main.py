import telegram
from telegram.ext import Updater, MessageHandler, Filters
import telegraph
import datetime

# Replace <YOUR_BOT_TOKEN> with your actual bot token
bot = telegram.Bot(token='6263204368:AAEtLDIrYTwAzWN-Qtk7LcYQXHvOGAIaSCY')

# Replace <YOUR_CHANNEL_NAME> with the name of the channel you want to collect posts from
channel_name = '@rk_update'

# Set up the telegraph instance
telegraph_api = telegraph.api.Telegraph()
telegraph_api.create_account(short_name='my_telegraph')

# Define the message handler
def handle_message(update, context):
    # Get the message from the update
    message = update.message.text
    
    # Check if the message is '/latest'
    if message == '/latest':
        # Get the latest post from the channel
        posts = bot.get_chat_history(chat_id=channel_name, limit=1)
        post = posts[0]
        
        # Create the telegra.ph page
        title = f"{post.chat.title} - {post.date.strftime('%m-%d-%y')}"
        content = post.text
        response = telegraph_api.create_page(title=title, content=[content])
        
        # Send the telegra.ph link to the user
        link = 'https://telegra.ph/{}'.format(response['path'])
        update.message.reply_text(link)

# Set up the message handler
updater = Updater(token='6263204368:AAEtLDIrYTwAzWN-Qtk7LcYQXHvOGAIaSCY', use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# Start the bot
updater.start_polling()
