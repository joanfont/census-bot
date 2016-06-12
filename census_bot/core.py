import telegram
from telegram.ext import Updater, MessageHandler, CommandHandler

from census_bot.helper import is_spanish_id
from census_bot import strings
from census_bot import config


class CensusBotFilters:
    @staticmethod
    def spanish_id(message):
        return message.text and not message.text.startswith('/') and is_spanish_id(message.text)

    @staticmethod
    def language(message):
        return message.text and not message.text.startswith('/') and message.text in strings.AVAILABLE_LANGUAGES

    @staticmethod
    def census(message):
        return message.text and not message.text.startswith('/') and message.text in config.AVAILABLE_CENSUS_NAMES


class CensusBot:
    def __init__(self, token, census_factory, settings_handler):
        self.updater = Updater(token=token)
        self.census_factory = census_factory
        self.settings_handler = settings_handler

    def configure_callbacks(self):
        dispatcher = self.updater.dispatcher

        dispatcher.add_handler(MessageHandler([CensusBotFilters.spanish_id], self.__find_handler))
        dispatcher.add_handler(MessageHandler([CensusBotFilters.language], self.__set_language_handler))
        dispatcher.add_handler(MessageHandler([CensusBotFilters.census], self.__set_census_handler))

        dispatcher.add_handler(CommandHandler('start', self.__start_handler))
        dispatcher.add_handler(CommandHandler('language', self.__language_handler))
        dispatcher.add_handler(CommandHandler('census', self.__census_handler))

    def __find_handler(self, bot, update):
        chat_id = update.message.chat_id
        user_id = update.message.from_user.id

        language = self.__get_user_language(user_id)
        census_client = self.__get_user_census(user_id)

        nif = update.message.text
        try:
            voter = census_client.find(nif)
            response = self.__response_formatter(voter, language)
        except census_client.APIError as e:
            response = str(e)

        bot.send_message(chat_id, response)

    def __start_handler(self, bot, update):
        chat_id = update.message.chat_id
        user_id = update.message.from_user.id
        language = self.__get_user_language(user_id)

        start_message = strings.START_MESSAGES.get(language)
        bot.send_message(chat_id, start_message)

    def __language_handler(self, bot, update):
        chat_id = update.message.chat_id
        user_id = update.message.from_user.id

        custom_keyboard = [strings.AVAILABLE_LANGUAGES]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)

        language = self.__get_user_language(user_id)
        select_language_message = strings.SELECT_LANGUAGE_MESSAGES.get(language)

        bot.send_message(chat_id, select_language_message, reply_markup=reply_markup)

    def __set_language_handler(self, bot, update):
        language = update.message.text

        if language not in strings.AVAILABLE_LANGUAGES:
            self.__language_handler(bot, update)

        chat_id = update.message.chat_id
        user_id = update.message.from_user.id

        self.__set_user_language(user_id, language)

        reply_markup = telegram.ReplyKeyboardHide()

        bot.send_message(chat_id, update.message.text, reply_markup=reply_markup)

    def __census_handler(self, bot, update):
        chat_id = update.message.chat_id
        user_id = update.message.from_user.id

        custom_keyboard = [config.AVAILABLE_CENSUS_NAMES]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)

        language = self.__get_user_language(user_id)
        select_census_message = strings.SELECT_CENSUS_MESSAGES.get(language)

        bot.send_message(chat_id, select_census_message, reply_markup=reply_markup)

    def __set_census_handler(self, bot, update):
        census = update.message.text

        if census not in config.AVAILABLE_CENSUS_NAMES:
            self.__census_handler(bot, update)

        chat_id = update.message.chat_id
        user_id = update.message.from_user.id

        self.__set_user_census(user_id, census)

        reply_markup = telegram.ReplyKeyboardHide()

        bot.send_message(chat_id, update.message.text, reply_markup=reply_markup)

    @staticmethod
    def __response_formatter(voter, language):
        message = strings.VOTER_MESSAGES.get(language)
        return message.format(
            district=voter.district,
            section=voter.section,
            table=voter.table,
            school=voter.school,
            address=voter.address
        )

    def __get_user_language(self, user_id):
        return self.settings_handler.get_language(user_id)

    def __set_user_language(self, user_id, language):
        language_key = strings.REVERSED_LANGUAGES_MAPPING.get(language)
        self.settings_handler.set_language(user_id, language_key)

    def __get_user_census(self, user_id):
        census_code = self.settings_handler.get_census(user_id)
        return self.census_factory.get(census_code)

    def __set_user_census(self, user_id, census):
        census_key = config.REVERSED_AVAILABLE_CENSUS_CODE_NAME_MAPPING.get(census)
        return self.settings_handler.set_census(user_id, census_key)

    def start(self):
        self.configure_callbacks()
        self.updater.start_polling()
        self.updater.idle()

    def stop(self):
        self.updater.stop()
