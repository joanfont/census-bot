import redis
from census_bot.config import REDIS_HOST, REDIS_PORT, DEFAULT_CENSUS, DEFAULT_LANGUAGE


class Handler:
    def __init__(self):
        self.redis = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)

    def set_language(self, user_id, language):
        key = self.__build_key(user_id, 'language')
        return self.redis.set(key, language)

    def get_language(self, user_id):
        key = self.__build_key(user_id, 'language')
        language = self.redis.get(key)
        return str(language, 'utf-8') if language else DEFAULT_LANGUAGE

    def set_census(self, user_id, census):
        key = self.__build_key(user_id, 'census')
        return self.redis.set(key, census)

    def get_census(self, user_id):
        key = self.__build_key(user_id, 'census')
        census = self.redis.get(key)
        return str(census, 'utf-8') if census else DEFAULT_CENSUS

    @staticmethod
    def __build_key(user_id, key):
        return '{user_id}::{key}'.format(user_id=user_id, key=key)

    def __get(self, key):
        return self.redis.get(key)

    def __set(self, key, value):
        return self.redis.set(key, value)
