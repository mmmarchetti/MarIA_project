# Telegram Bot for OpenAI GPT-3 Text and Image Generation
This repository contains the code for a Telegram bot that uses OpenAI's GPT-3 to generate text and images based on user input.

### Getting Started
To use the bot, you will need to have a Telegram account and create a bot through the BotFather. Once you have created a bot, you will receive a token that you will need to provide in a .env file in the root directory of the project.

* TELEGRAM_BOT_TOKEN = "your-telegram-bot-token"
* OPENAI_API_KEY = "your-openai-api-key"

You will also need to have an OpenAI API key to use the GPT-3 API. You can obtain an API key by signing up for OpenAI here.

### Prerequisites
To run the bot, you will need to have Python 3 installed. You can download Python 3 from the official website: https://www.python.org/downloads/

### Installing
To install the required dependencies, run:

$pip install -r requirements.txt

### Running the Bot
To run the bot, simply run the following command in the root directory of the project:

$python main.py

The bot will listen for messages sent to it on Telegram and respond with either generated text or an image, depending on the input.

### Built With

Python 3
Telegram API
OpenAI API

### Authors
* OpenAI - Initial work - OpenAI
* Marcos Martins Marchetti - Additional work

License
This project is licensed under the MIT License - see the LICENSE file for details.
