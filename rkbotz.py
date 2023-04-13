import pyrogram
import telegraph
import datetime

# Replace <YOUR_BOT_TOKEN> with your actual bot token
bot = pyrogram.Client('my_bot', bot_token='6263204368:AAEtLDIrYTwAzWN-Qtk7LcYQXHvOGAIaSCY')

# Replace <YOUR_CHANNEL_NAME> with the name of the channel you want to collect posts from
channel_name = '@rk_update'

# Set up the telegraph instance
telegraph_api = telegraph.api.Telegraph()
telegraph_api.create_account(short_name='my_telegraph')

# Define the message handler
def handle_message(client, message):
    # Get the message text
    text = message.text
    
    # Check if the message is '/latest'
    if text == '/latest':
        # Get the latest post from the channel
        posts = client.get_history(channel_name, limit=1)
        post = posts[0]
        
        # Create the telegra.ph page
        title = f"{post.chat.title} - {post.date.strftime('%m-%d-%y')}"
        content = post.text
        response = telegraph_api.create_page(title=title, content=[content])
        
        # Send the telegra.ph link to the user
        link = 'https://telegra.ph/{}'.format(response['path'])
        client.send_message(message.chat.id, link)

# Start the bot
bot.add_handler(pyrogram.MessageHandler(pyrogram.Filters.text & ~pyrogram.Filters.command, handle_message))
bot.run()
