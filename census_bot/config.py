import dotenv as env
import os

env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../.env'))

env.load_dotenv(env_path)

TOKEN = os.getenv('TOKEN')

CENSUS_URL = os.getenv('CENSUS_URL')

