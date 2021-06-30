from config import Config
from requests import Session
from datetime import datetime
from numerize import numerize

"""
**************************************************
Class CryptoCurrency
Paramaters: Crypto data

serialize and filter the data
format large numbers to human readable format
returns the formated object

**************************************************
"""
class CryptoCurrency(object):
    def __init__(self, data):
        self.name = data["name"]
        self.symbol = data['symbol']
        self.slug = data['slug']
        self.price = data["quote"]["USD"]["price"]
        self.volume_24h = int(data["quote"]["USD"]["volume_24h"])
        self.percent_change_24h = data["quote"]["USD"]["percent_change_24h"]
        self.circulating_supply = int(data["circulating_supply"])
        self.market_cap = int(data["quote"]["USD"]["market_cap"])
    
    def format_currency(self):
        self.price = "${:,.3f}".format(self.price)
        self.percent_change_24h = "{:.2f}".format(self.percent_change_24h)
        self.volume_24h = numerize.numerize(self.volume_24h)
        self.circulating_supply = numerize.numerize(self.circulating_supply)
        self.market_cap = numerize.numerize(self.market_cap)

    def get_currency(self):
        return {
            "name":self.name,
            "symbol":self.symbol,
            "slug": self.slug,
            "price":self.price,
            "volume_24h":self.volume_24h,
            "percent_change_24h":self.percent_change_24h,
            "circulating_supply":self.circulating_supply,
            "market_cap":self.market_cap
        }
""""
**************************************************
Function: get_all_crypto_data
Paramaters: Coinmarketcap api key

get all crypto currencies
serialize and format each one of the crypto data.
inserting the objects to a list and return it

**************************************************

"""
def get_all_crypto_currency_data(api_key):
    crypto_currencies_list = []
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    headers = {
        "Accepts":"application/json",
        "X-CMC_PRO_API_KEY": api_key
    }
    session = Session()
    res = session.get(url, headers=headers)
    crypto_data_list = res.json()['data']
    for data in crypto_data_list:
        crypto_object = CryptoCurrency(data)
        crypto_object.format_currency()
        crypto_currencies_list.append(crypto_object.get_currency())
    
    return crypto_currencies_list

""""
**************************************************
Function: filter_by_keyword
Paramaters: user input, list of crypto objects

checks the user input if the length is 3 chars
if so, it will be most likely a symbol of a crypto
so we will change it to uppercase letters.
check if the user input matches one of the filter
options and returns the crypto object if true

**************************************************

"""
def filter_by_keyword(keyword, crypto_list):
    for crypto in crypto_list:
        if len(keyword) == 3:
            keyword = keyword.upper()
        filter_options = [crypto['name'], crypto['slug'], crypto['symbol']]
        if keyword in filter_options:
            return crypto
    return

""""
**************************************************
Function: get_response
Paramaters: user input

get data of all crypto currency
filter it by the user input
return the crypto currency

**************************************************

"""
def get_response(user_input):
    COINMARKETCAP_API_KEY = Config.COINMARKETCAP_API_KEY
    crypto_list = get_all_crypto_currency_data(COINMARKETCAP_API_KEY)
    crypto = filter_by_keyword(user_input, crypto_list)
    return crypto


""""
**************************************************
Function: get_formated_text
Paramaters: crypto currency object 

get the datetime in a readable format
returns a detailed message to send as a response

**************************************************

"""
def get_formated_text(obj):
    now = datetime.now()
    formated_datetime = now.strftime("%d/%m/%y, %H:%M:%S")
    return f"""
    *****************************
    Name: {obj["name"]}
    Symbol: {obj["symbol"]}
    Price: {obj["price"]}
    Volume 24h: {obj["volume_24h"]}
    Percent 24h Change: {obj["percent_change_24h"]}%
    Circulating Supply: {obj["circulating_supply"]}
    Market Cap: {obj["market_cap"]}

    Date & Time: {formated_datetime}
    ******************************

    """

""""
**************************************************
Function: get_help

returns a detailed message to guide the user how
to use the bot. 

**************************************************

"""
def get_help():
    return f"""
    ******************************
    Welcome to the crypto group!
    I'm CryptoUpdaterBot :) 
    My Job is to keep you updated
    with all the info about crypto.

    For your convenience you dont need
    to write / before searching for info
    and you dont need to worry about capital
    letters either.

    There are few ways to get crypto
    info:
    
    1)By Symbol: type the crypto
      symbol (Example: BTC).
    
    2)By Name: type the crypto
      Name (Example: Bitcoin).

    ******************************    

    """


if __name__ == '__main__':
    print("testing")
    


        