from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from lesson1.tokens import bot_token
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

answer = {"привет": "И тебе привет!", "как дела?": "Лучше всех", "пока": "Увидимся"}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(update)
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    question = update.message.text
    print(question)
    if question in answer:
        update.message.reply_text(answer[question])
    else:
        update.message.reply_text("Ну здрасте")


def main(token = bot_token):
    updater = Updater(str(token))

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    updater.start_polling()
    updater.idle()


main()
