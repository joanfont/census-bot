import redis
from census_bot.config import REDIS_HOST, REDIS_PORT
from census_bot.strings import DEFAULT_LANGUAGE


class Handler:
    def __init__(self):
        self.redis = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)

    def set_language(self, user_id, language):
        key = self.__build_key(user_id, 'language')
        return self.redis.set(key, language)

    def get_language(self, user_id):
        key = self.__build_key(user_id, 'language')
        language = self.redis.get(key) or DEFAULT_LANGUAGE
        return str(language, 'utf-8')

    @staticmethod
    def __build_key(user_id, key):
        return '{user_id}::{key}'.format(user_id=user_id, key=key)

    def __get(self, key):
        return self.redis.get(key)

    def __set(self, key, value):
        return self.redis.set(key, value)
