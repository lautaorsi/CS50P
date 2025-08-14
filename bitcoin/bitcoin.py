import requests
import sys
r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
try:
    amount = sys.argv[1]
    amount = float(amount)
except TypeError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")
else:
    rjs = r.json()['bpi']
    currency = rjs['USD']
    amnt = currency['rate_float'] * amount
    output = float(amnt)
    print(f'${output:,.4f}')

