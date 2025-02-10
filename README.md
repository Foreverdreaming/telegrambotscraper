<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Telegram RSS Feed Bot</title>
</head>
<body>
    <h1>Telegram RSS Feed Bot</h1>
    <p>A Python-based Telegram bot that retrieves and displays RSS feed data. Users can choose between different RSS feeds, refresh the feed, and perform other follow-up actions using the bot.</p>

    <h2>Setup Instructions</h2>

    <h3>1. Prerequisites</h3>
    <ul>
        <li>Python 3.6 or later installed on your system.</li>
        <li>Telegram Bot API token (obtain from <a href="https://t.me/BotFather" target="_blank">BotFather</a>).</li>
        <li>The following Python packages:
            <ul>
                <li><code>pyTelegramBotAPI</code></li>
                <li><code>feedparser</code></li>
            </ul>
        </li>
    </ul>

    <h3>2. Install Dependencies</h3>
    <pre><code>pip install pyTelegramBotAPI feedparser</code></pre>

    <h3>3. Clone the Project</h3>
    <pre><code>git clone https://github.com/yourusername/telegram-rss-feed-bot.git
cd telegram-rss-feed-bot</code></pre>

    <h3>4. Update the Script</h3>
    <p>Replace the placeholder <code>YOUR_BOT_TOKEN</code> with your actual Telegram Bot API token in the <code>scraper.py</code> file. Modify the <code>RSS_FEEDS</code> dictionary to include your desired RSS feed URLs.</p>
    <pre><code>
RSS_FEEDS = {
    "Feed 1": "https://example.com/rss1",
    "Feed 2": "https://example.com/rss2"
}
    </code></pre>

    <h3>5. Run the Bot</h3>
    <pre><code>python scraper.py</code></pre>

    <hr>

    <h2>Bot Commands</h2>
    <table border="1" cellspacing="0" cellpadding="5">
        <thead>
            <tr>
                <th>Command</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>/start</td>
                <td>Start the bot and display a welcome message.</td>
            </tr>
            <tr>
                <td>/choose</td>
                <td>Show a menu to select an RSS feed.</td>
            </tr>
            <tr>
                <td>/rss</td>
                <td>(Optional) Manually trigger RSS feed retrieval.</td>
            </tr>
        </tbody>
    </table>

    <hr>