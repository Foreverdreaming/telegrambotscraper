import telebot
import feedparser
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


# Your Telegram bot token from BotFather
# BOT_TOKEN = "YOUR_TELEGRAMBOT_TOKEN"

# # RSS feed URLs
# RSS_FEEDS = {
#     "Feed 1": "https://www.example.com/feed1/",
#     "Feed 2": "https://www.example.com/feed2/"
# }

bot = telebot.TeleBot(BOT_TOKEN)
user_last_feed = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Send a welcome message with instructions."""
    bot.reply_to(message, "Welcome to Cyber Security News Bot! Use /choose to select your desired news letter.")



@bot.message_handler(commands=['choose'])
def choose_feed(message):
    """Present the user with feed choices."""
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton("Feed1"), KeyboardButton("Feed2"))

    bot.send_message(message.chat.id, "Choose a feed:", reply_markup=markup)



@bot.message_handler(func=lambda msg: msg.text in RSS_FEEDS)
def send_rss_feed(message):
    """Fetch and send RSS feed based on the user's choice."""
    feed_url = RSS_FEEDS[message.text]

    user_last_feed[message.chat.id] = message.text

    feed = feedparser.parse(feed_url)

    if feed.bozo:
        bot.reply_to(message, "Failed to retrieve RSS feed.")
    else:
        response = "Feed Title: {}\n\n".format(feed.feed.title)
        for entry in feed.entries[:5]:
            response += "Title: {}\n".format(entry.title)
            response += "Link: {}\n".format(entry.link)
            response += "Published: {}\n".format(entry.get("published", "No publish date"))
            response += "Summary: {}\n\n".format(entry.get("summary", "No summary available"))
            response += "-" * 40 + "\n"

        bot.reply_to(message, response)

        show_follow_up_options(message)

def show_follow_up_options(message):
    """Show follow-up options after displaying the feed."""
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Choose another feed", callback_data='choose_feed'),
        InlineKeyboardButton("Refresh current feed", callback_data='refresh_feed'),
        InlineKeyboardButton("End interaction", callback_data='end_interaction')
    )
    bot.send_message(message.chat.id, "What would you like to do next?", reply_markup=markup)

# Step 4: Handle follow-up actions using callbacks
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    """Handle user choices for follow-up actions."""
    if call.data == 'choose_feed':
        choose_feed(call.message)
    elif call.data == 'refresh_feed':
        # Get the last selected feed and refresh it
        last_feed = user_last_feed.get(call.message.chat.id)
        if last_feed:
            call.message.text = last_feed  # Simulate user selecting the last feed again
            send_rss_feed(call.message)
        else:
            bot.send_message(call.message.chat.id, "No previous feed to refresh. Use /choose to select a feed.")
    elif call.data == 'end_interaction':
        bot.send_message(call.message.chat.id, "Thank you for using the bot. Have a great day! Use /start to start again.")


bot.polling()
