import logging

logger = logging.getLogger('census_bot')
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('log/census_bot.log')
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)

logger.addHandler(handler)