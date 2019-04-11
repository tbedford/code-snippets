# Just a simulation of a freal-time data feed
from threading import Timer
import datetime
import re

def get_utc_timestamp ():
    time_now = str(datetime.datetime.utcnow())
    m = re.search(r'(\d\d\d\d-\d\d-\d\d) (\d\d:\d\d:\d\d)', time_now)
    return m.group(1) + ' ' + m.group(2) + ' UTC'

prices = {
    'MSFT': ['120.24', '119.36', '118.34', '119.78', '120.23', '122.98', '140.21', '141.09', '144.98', '155.92', '170.19'],
    'GOOGL': ['1209.24', '1209.66', '1299.54', '1300.19', '1327.26', '1299.12', '1300.00', '11301.91', '1308.67', '1350.11', '1400.01'],
}

delay = 5
tic_count = 0
symbol = "MSFT"

def stocks():
    global tic_count
    t = Timer(delay, stocks)
    t.start()
    print("%d. [%s] %s: %s" % (tic_count, get_utc_timestamp(), symbol, prices[symbol][tic_count]))
    if tic_count < len(prices[symbol])-1: 
        tic_count = tic_count + 1
    else:
        tic_count = 0
    return

stocks()

