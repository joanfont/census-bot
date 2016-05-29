import requests


class APIError(Exception):
    pass


class NifRequiredError(APIError):
    pass


class InvalidNifError(APIError):
    pass


class Voter:
    def __init__(self, nif, district, section, table, school, address):
        self.nif = nif
        self.district = district
        self.section = section
        self.table = table
        self.school = school
        self.address = address

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


class ElectoralCensusClient:
    FIND_ENDPOINT = '/find'

    STATUS_CODE_EXCEPTION_MAPPING = {
        requests.codes.bad_request: NifRequiredError,
        requests.codes.not_found: InvalidNifError,
    }

    APIError = APIError
    NifRequiredError = NifRequiredError
    InvalidNifError = InvalidNifError

    def __init__(self, base_url):
        self.base_url = base_url

    def find(self, nif):
        url = '{base}{endpoint}?nif={nif}'.format(
            base=self.base_url,
            endpoint=self.FIND_ENDPOINT,
            nif=nif
        )

        response = requests.get(url, verify=False)
        status_code = response.status_code
        body = response.json()

        if status_code in self.STATUS_CODE_EXCEPTION_MAPPING:
            error_class = self.STATUS_CODE_EXCEPTION_MAPPING.get(status_code)
            error_desc = body.get('error_desc')
            raise error_class(error_desc)

        return Voter(**body)
