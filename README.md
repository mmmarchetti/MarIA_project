# Telegram AI Bot

This is a simple AI bot that uses OpenAI to generate responses to user inputs on Telegram. The bot is able to generate either text or image responses based on the user input.

## Installation

To run this bot, you will need to have Python 3.6 or higher installed on your computer.

1. Clone the repository:
    ```
    git clone https://github.com/your_username/telegram-ai-bot.git
    ```

2. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

3. Create a `.env` file and add your Telegram bot token and OpenAI API key:
    ```
    TELEGRAM_BOT_TOKEN=your_telegram_bot_token
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

To start the bot, run the following command in your terminal:
    ```
    python main.py
    ```

Once the bot is running, you can interact with it on Telegram by sending it messages.

The bot will respond with either text or image based on the user input. If the user input contains any of the words "imagem", "desenho", "desenhe", "figura", "image", "figure", "drawing", or "drawn", the bot will generate an image response using OpenAI's image API. Otherwise, the bot will generate a text response using OpenAI's text API.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
