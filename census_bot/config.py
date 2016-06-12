import os
import yaml
import functools

config_yml_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../config.yml'))
with open(config_yml_path, 'r') as f:
    config = yaml.safe_load(f)

TOKEN = config.get('telegram').get('token')

DEFAULT_LANGUAGE = config.get('language').get('default')

CENSUS = config.get('census')
DEFAULT_CENSUS = CENSUS.get('default')
AVAILABLE_CENSUS = CENSUS.get('available')
AVAILABLE_CENSUS_KEYS = AVAILABLE_CENSUS.keys()


def __build_census_code_name_mapping(carry, current):
    carry[current] = AVAILABLE_CENSUS.get(current).get('name')
    return carry


AVAILABLE_CENSUS_CODE_NAME_MAPPING = functools.reduce(__build_census_code_name_mapping, AVAILABLE_CENSUS_KEYS, {})
AVAILABLE_CENSUS_NAMES = AVAILABLE_CENSUS_CODE_NAME_MAPPING.values()
REVERSED_AVAILABLE_CENSUS_CODE_NAME_MAPPING = dict((v, k) for k, v in AVAILABLE_CENSUS_CODE_NAME_MAPPING.items())

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
