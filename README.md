# census-bot
a Telegram bot for consulting the electoral census of Palma

## Usage

### With python `virtualenv`

* First make sure you have [redis](http://redis.io/) installed.
* Create a Python virtualenv and install the package requirements.
* Create a `config.yml` file with the `config.yml.sample` as a template.
* Run `python3 main.py` and the script will process any message received and return the census info.

### With docker

* Create a `config.yml` file with the `config.yml.sample` as a template.
* First start your redis instance: `docker run -d --name redis library/redis:3.2.0`
* Run `docker run --link redis:redis -e "REDIS_HOST=redis" -e "REDIS_PORT=6379" -v ${PWD}/config.yml:/code/config.yml joanfont/census-bot`


## Add your data providers

In `config.yml` file you can specify the census data providers' bot can use. You can add yours:

```yml
census:
  default: palma
  available:
    palma:
      name: Palma
      url: https://cens.joan-font.cat
    inca:
      name: Inca
      url: http://cens.incaciutat.com
```

The census data provider endpoint (`/find?nif=44444444A`) must return a response like this one: 
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