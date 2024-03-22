# Anzor's Telegram Bot

An interactive Telegram bot built using Python, Telebot, and PyTube to download YouTube videos based on user-provided links.


## Features

- Downloads YouTube videos when users provide valid video links.
- Sends downloaded videos back to users in Telegram chat.
- Automatically sends an introductory message when users start a chat with the bot.
  

## Installation

In order to use this code you will need to create a new telegram bot model using @BotFather. 

Find @BotFather in your Telegram and type /newbot - follow the simple instructions. 


To run this bot locally, follow these steps:

1. **Clone the repository:** `git clone https://github.com/your-username/anzor-telegram-bot.git`

2. **Create a `.env` file** in the root directory and add your Telegram Bot token:

     BOT_TOKEN=your_telegram_bot_token

3. **Run the bot:** `python3 bot.py`


## Usage

1. Start downloading with the bot by searching for it on Telegram as "AnzDev" and clicking "Start" or
   create your own using Installation section above.

3. Send a YouTube video link in the chat.

4. The bot will download the video and send it back to you in the chat.
   

## Commands

- **/start**: Start the bot and receive an introductory message.
- **/hello**: Get a greeting message from the bot.
  

## Dependencies

The bot uses the following APIs and libraries:

- **Telebot**: A Python library for building Telegram bots.
- **PyTube**: A library for downloading YouTube videos.
  
Make sure to install these dependencies using `pip3 install telebot pytube` before running the bot.


## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.


## License

This project is unlicensed.
