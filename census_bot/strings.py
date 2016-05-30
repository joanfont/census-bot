START_MESSAGE = '''
    Benvingut al bot per consultar la informació del Cens Electoral de Palma.''' \
                    u'''Podràs rebre la informació d'on et toca anar a votar (districte, secció, mesa, col·legi i adreça). \n\n''' \
                    '''Per començar escriu el teu NIF i consulta la teva informació censal'''

VOTER_MESSAGE = 'Districte: {district}\nSecció: {section}\nMesa: {table}\nCol·legi: {school}\nDirecció: {address}'

AVAILABLE_LANGUAGES = [
    'Català',
    'Castellà'
]

SELECT_LANGUAGE = '''Tria l'idioma que vols utilitzar'''