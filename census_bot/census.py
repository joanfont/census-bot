from census_bot.api import ElectoralCensusClient


class Factory:

    def __init__(self, census, default_census_code):
        self.census = census
        self.default_census_code = default_census_code

    def get(self, item):
        return self.census.get(item, self.default_census_code)

    @classmethod
    def from_config(cls, config):
        census = {}

        default = config.get('default')
        available = config.get('available')

        for census_code, census_data in available.items():
            census_name = census_data.get('name')
            census_url = census_data.get('url')

            census[census_code] = ElectoralCensusClient(census_name, census_code, census_url)

        return cls(census, default)

