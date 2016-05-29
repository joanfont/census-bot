from telegram.ext import Updater, MessageHandler, Filters
from functools import partial
from census_bot.api import ElectoralCensusClient


class CensusBot:
    def __init__(self, token, census_client):
        self.updater = Updater(token=token)
        self.census_client = census_client

    def configure_callbacks(self):
        dispatcher = self.updater.dispatcher

        handler_partial = partial(self.__handler,
                                  census_client=self.census_client,
                                  response_formatter=self.__voter_formatter
                                  )
        dispatcher.add_handler(MessageHandler([Filters.text], handler_partial))

    @staticmethod
    def __handler(bot, update, census_client=None, response_formatter=None):
        if not census_client or not isinstance(census_client, ElectoralCensusClient):
            return

        if not callable(response_formatter):
            return

        chat_id = update.message.chat_id
        nif = update.message.text
        try:
            voter = census_client.find(nif)
            response = response_formatter(voter)
        except census_client.APIError as e:
            response = str(e)

        bot.send_message(chat_id, response)

    @staticmethod
    def __voter_formatter(voter):
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