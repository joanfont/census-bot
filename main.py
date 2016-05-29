from census_bot.api import ElectoralCensusClient
from census_bot.core import CensusBot

from census_bot import config

client = ElectoralCensusClient(config.CENSUS_URL)
bot = CensusBot(config.TOKEN, client)

if __name__ == '__main__':
    bot.start()
