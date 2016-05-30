import telegram
from telegram.ext import Updater, MessageHandler, CommandHandler

from census_bot.api import ElectoralCensusClient
from census_bot.helper import is_spanish_id
from census_bot import strings


class CensusBotFilters:
    @staticmethod
    def spanish_id(message):
        return message.text and not message.text.startswith('/') and is_spanish_id(message.text)

    @staticmethod
    def language(message):
        return message.text and not message.text.startswith('/') and message.text in strings.AVAILABLE_LANGUAGES


class CensusBot:
    def __init__(self, token, census_client):
        self.updater = Updater(token=token)
        self.census_client = census_client

    def configure_callbacks(self):
        dispatcher = self.updater.dispatcher

        dispatcher.add_handler(MessageHandler([CensusBotFilters.spanish_id], self.__find_handler))
        dispatcher.add_handler(MessageHandler([CensusBotFilters.language], self.__set_language_handler))

        dispatcher.add_handler(CommandHandler('start', self.__start_handler))
        dispatcher.add_handler(CommandHandler('language', self.__language_handler))

    def __find_handler(self, bot, update):
        if not self.census_client or not isinstance(self.census_client, ElectoralCensusClient):
            return

        chat_id = update.message.chat_id
        nif = update.message.text
        try:
            voter = self.census_client.find(nif)
            response = self.__response_formatter(voter)
        except self.census_client.APIError as e:
            response = str(e)

        bot.send_message(chat_id, response)

    @staticmethod
    def __start_handler(bot, update):
        chat_id = update.message.chat_id
        bot.send_message(chat_id, strings.START_MESSAGE)

    @staticmethod
    def __language_handler(bot, update):
        chat_id = update.message.chat_id
        custom_keyboard = [strings.AVAILABLE_LANGUAGES]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        bot.send_message(chat_id, strings.SELECT_LANGUAGE, reply_markup=reply_markup)

    @classmethod
    def __set_language_handler(cls, bot, update):
        message = update.message.text
        if message not in strings.AVAILABLE_LANGUAGES:
            cls.__language_handler(bot, update)

        chat_id = update.message.chat_id
        bot.send_message(chat_id, update.message.text)

    @staticmethod
    def __response_formatter(voter):
        return strings.VOTER_MESSAGE.format(
            district=voter.district,
            section=voter.section,
            table=voter.table,
            school=voter.school,
            address=voter.address
        )

    def start(self):
        self.configure_callbacks()
        self.updater.start_polling()
        self.updater.idle()

    def stop(self):
        self.updater.stop()
