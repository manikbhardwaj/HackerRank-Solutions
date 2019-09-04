from datetime import datetime
from datetime import timedelta
import urllib.request
import json


def getResponse(url):
    operUrl = urllib.request.urlopen(url)
    if (operUrl.getcode() == 200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())
    return jsonData

def get_next_weekday(startdate, weekday):
    """
    @startdate: given date, in format '2013-05-25'
    @weekday: week day as a integer, between 0 (Monday) to 6 (Sunday)
    """
    d = datetime.strptime(startdate, '%Y-%m-%d %H:%M:%S')
    t = timedelta((7 + weekday - d.weekday()) % 7)
    return (d + t).strftime('%Y-%m-%d')


def openAndClosePrices(firstDate, lastDate, weekDay):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    startDate = datetime.strptime("5-January-2000", "%d-%B-%Y")
    endDate = datetime.strptime("1-January-2014", "%d-%B-%Y")
    fromDate = datetime.strptime(firstDate, "%d-%B-%Y")
    toDate = datetime.strptime(lastDate, "%d-%B-%Y")
    if fromDate < startDate:
        fromDate = startDate
    if toDate > endDate:
        toDate = endDate

    if weekDay not in weekdays:
        print("out of parameters")
    else:
        while True:
            index = weekdays.index(weekDay)
            newDate = get_next_weekday(f'{fromDate}', index)
            temp_date = datetime.strptime(newDate, "%Y-%m-%d")
            temp_date2 = temp_date.strftime("%#d-%B-%Y")
            urlData = f"https://jsonmock.hackerrank.com/api/stocks/?date={temp_date2}"
            jsonData = getResponse(urlData)

            if jsonData['total'] == 0:
                fd = (temp_date + timedelta(days=7)).strftime('%#d-%B-%Y')
                fromDate = datetime.strptime(fd, "%d-%B-%Y")
            else:
                for i in jsonData["data"]:
                    print(f'{i["date"]} {i["open"]} {i["close"]}')
                    fd = (temp_date + timedelta(days=7)).strftime('%#d-%B-%Y')
                    fromDate = datetime.strptime(fd, "%d-%B-%Y")

            if (fromDate > toDate):
                break


try:
    _firstDate = "1-January-2000"
except:
    _firstDate = None

try:
    _lastDate = "22-February-2000"
except:
    _lastDate = None

try:
    _weekDay = "Monday"
except:
    _weekDay = None

openAndClosePrices(_firstDate, _lastDate, _weekDay)