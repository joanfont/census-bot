from census_bot.core import CensusBot
from census_bot.settings import Handler as SettingsHandler
from census_bot.census import Factory as CensusFactory

from census_bot import config

census_factory = CensusFactory.from_config(config.CENSUS)
settings_handler = SettingsHandler()

bot = CensusBot(config.TOKEN, census_factory, settings_handler)

if __name__ == '__main__':
    bot.start()
