import re

NIF_REGEX = re.compile('^(\d{8})([TRWAGMYFPDXBNJZSQVHLCKE]{1})$', re.IGNORECASE)
NIE_REGEX = re.compile('^([XYZ]{1})(\d{7})([TRWAGMYFPDXBNJZSQVHLCKE]{1})$', re.IGNORECASE)


def is_spanish_id(nif):
    return NIF_REGEX.match(nif) or NIE_REGEX.match(nif)
