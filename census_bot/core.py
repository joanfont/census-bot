from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from functools import partial
from census_bot.api import ElectoralCensusClient


class CensusBot:

    START_MESSAGE = '''
    Benvingut al bot per consultar la informació del Cens Electoral de Palma.''' \
    u'''Podràs rebre la informació d'on et toca anar a votar (districte, secció, mesa, col·legi i adreça). \n\n''' \
    '''Per començar escriu el teu NIF i consulta la teva informació censal'''

    VOTER_MESSAGE = 'Districte: {district}\nSecció: {section}\nMesa: {table}\nCol·legi: {school}\nDirecció: {address}'


    def __init__(self, token, census_client):
        self.updater = Updater(token=token)
        self.census_client = census_client

    def configure_callbacks(self):
        dispatcher = self.updater.dispatcher

        find_handler_partial = partial(self.__find_handler)
        start_handler_partial = partial(self.__start_handler)

        dispatcher.add_handler(MessageHandler([Filters.text], find_handler_partial))
        dispatcher.add_handler(CommandHandler('start', start_handler_partial))

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

    def __start_handler(self, bot, update):
        chat_id = update.message.chat_id
        bot.send_message(chat_id, self.START_MESSAGE)

    @staticmethod
    def __response_formatter(voter):
        return '''
        Districte: {district}\nSecció: {section}\nMesa: {table}\nCol·legi: {school}\nDirecció: {address}'''.format(
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
