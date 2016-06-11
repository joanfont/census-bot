from census_bot.api import ElectoralCensusClient
from census_bot.core import CensusBot
from census_bot.settings import Handler as SettingsHandler

from census_bot import config

census_client = ElectoralCensusClient(config.CENSUS_URL)
settings_handler = SettingsHandler()

bot = CensusBot(config.TOKEN, census_client, settings_handler)

if __name__ == '__main__':
    bot.start()
