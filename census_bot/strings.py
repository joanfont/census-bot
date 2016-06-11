START_MESSAGES = {
    'ca': u''' Benvingut al bot per consultar la informació del Cens Electoral de Palma.'''
          u'''Podràs rebre la informació d'on et toca anar a votar (districte, secció, mesa, col·legi i adreça). \n\n'''
          u'''Per començar escriu el teu NIF i consulta la teva informació censal''',

    'es': u'''Bienvenido al bot para consultar la información del Censo Electoral de Palma.'''
          u'''Podrás recibir la información de donde te tocar ir a votar (distrito, sección, mesa, colegio y dirección.) \n\n'''
          u'''Para empezar, escribe tu NIF y consulta tu información censal'''

}

VOTER_MESSAGES = {
    'ca': 'Districte: {district}\nSecció: {section}\nMesa: {table}\nCol·legi: {school}\nDirecció: {address}',
    'es': 'Distrito: {district}\nSección: {section}\nMesa: {table}\nColegio: {school}\nDirección: {address}'
}

SELECT_LANGUAGE_MESSAGES = {
    'ca': '''Tria l'idioma que vols utilitzar''',
    'es': '''Escoge el idioma que quieres utilizar'''
}


LANGUAGES_MAPPING = {
    'ca': 'Català',
    'es': 'Castellà',
}

REVERSED_LANGUAGES_MAPPING = dict((v, k) for (k, v) in LANGUAGES_MAPPING.items())
AVAILABLE_LANGUAGES = LANGUAGES_MAPPING.values()

DEFAULT_LANGUAGE = 'ca'
