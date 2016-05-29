# census-bot
a Telegram bot for consulting the electoral census of Palma

## Usage

### With python `virtualenv`

* Create a Python virtualenv and install the package requirements.
* Create a `.env` file with `CENSUS_URL` and `TOKEN` values.
* Run `python3 main.py` and the script will process any message received and return the census info.

### With docker
* Run `docker run -e "TOKEN={{ your telegram token }}" -e "CENSUS_URL={{ your census provider url }} joanfont/census-bot`


## Use a different census data provider

If you forked the repository that provides census data ([electoral-census](https://www.github.com/joanfont/electoral-census)), 
you only have to provide an API base URL that implements the endpoint `/find?nif=44444444A` that returns a JSON like this:

```javascript
{
    "address": "CA PABLO IGLESIAS  4 , 07004 PALMA",
    "district": ​3,
    "nif": "44444444A",
    "school": "COL.LEGI SANT RAFAEL",
    "section": ​2,
    "table": "A"
}
```


##### Disclaimer
This bot only makes requests to an API that provides census data. It does not have any relation with Ajuntament de Palma. 
The data is consulted in the Ajuntament de Palma [census page](http://cens.palmademallorca.es/cens/dinamic/Consulta.htm).
You can see the API's code in the following GitHub respository: [electoral-census](https://www.github.com/joanfont/electoral-census).