from data.config import API_KEY
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': str(API_KEY),
}

session = Session()
session.headers.update(headers)

coin_dict = {'BTC': 'BTC: Bt7357hggjk63ffjlcszxvb53fs256gfsjjch531j',
             'ETH': 'ETH: Eth99357hggjk63ffjlcszxvb53fs256gffgh531j',
             'USDT': 'USDT trc20: trc257hggjk63ffjlcszxvb53fs256gfsjjch531j',
             'XMR': 'XMR: XMR357hggjk63ffjlcszxvb53fs256gfsjjch531j',
             'ZEC': 'ZEC: LTc357hggjk63ffjlcszxvb53fs256gfsjjch531j',
             'LTC': 'LTC: Bt7357hggjk63ffjlcszxvb53fs256gfsjjch531j'}

actual_cost = {}

try:
    response = session.get(url)
    data = json.loads(response.text)
    for i in data['data']:
        if i['symbol'] in coin_dict:
            actual_cost[i['symbol']] = (i['quote']['USD']['price'], i['last_updated'])
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

actual_cost['USDT trc20'] = actual_cost['USDT']
actual_cost.pop('USDT')
