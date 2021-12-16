from datetime import datetime, timedelta, date
import requests
import json

### API
def actual_api(curr):
    try:
        api_call = requests.get(f"https://api.coindesk.com/v1/bpi/currentprice/{curr}.json")
        api = json.loads(api_call.content)
    except:
        print("Error in input in API or error from CoinDesk.")
    return api

def history_api(a, b):
    try:
        api_call = requests.get(f"https://api.coindesk.com/v1/bpi/historical/close.json?start={a}&end={b}")
        apiH = json.loads(api_call.content)
    except:
        print("Error in input in API or error from CoinDesk.")
    return apiH


### DATE
def call_time():
    year, month, day = int(datetime.now().strftime("%Y")), int(datetime.now().strftime("%m")), int(datetime.now().strftime("%d"))
    hour, minute, second = int(datetime.now().strftime("%H")), int(datetime.now().strftime("%M")), int(datetime.now().strftime("%S"))
    return (year, month, day, hour, minute, second)


def daterange(start_date, end_date): # Date loop
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def check_string_date(a, b): # adding zeros to match needs
    if a[6:7] == "-":
        a = a[:5] + "0" + a[5:]
    if len(a) != 10:
        a = a[:8] + "0" + a[8:]
    if b[6:7] == "-":
        b = b[:5] + "0" + b[5:]
    if len(b) != 10:
        b = b[:8] + "0" + b[8:]
    return a, b


def date_loop_logic(a, b):
    x = []
    a, b = check_string_date(a, b)

    year1, month1, day1 = int(a[:4]), int(a[5:7]), int(a[8:11])
    year2, month2, day2 = int(b[:4]), int(b[5:7]), int(b[8:11])
    start_date = date(year1, month1, day1)
    end_date = date(year2, month2, day2)
    for single_date in daterange(start_date, end_date):
        x.append(single_date.strftime("%Y-%m-%d"))
    return x, a, b

def date_loop(a, b): # Get date from beginning to end
    x, a, b = date_loop_logic(a, b)
    y = unwrap_data(x, a, b)
    if len(y) != len(x):
        x.pop()
    return (y, x)


def unwrap_data(x, a, b): #Unwrap data to price
    c = []
    apiH = history_api(a, b)
    for i in x:
        try:
            c.append(apiH["bpi"][i])
        except:
            print("Error in unwraping data. Propably date isn't updated within api. *Ignore*")
    return c
