import csv
import urllib2
import finance as fin
import datetime as dt
from StringIO import StringIO as sIO
	
	
source = 'http://ichart.finance.yahoo.com/table.csv?s='
dateFormat = "%Y-%m-%d"

def getHistoricalPrices(stockSymbol):
	req = urllib2.urlopen(source+stockSymbol)
	prices = req.read()
	dReader = csv.DictReader(sIO(prices))
	histPrices = [fin.AssetPrice(dt.datetime.strptime(row['Date'], dateFormat).date(), row['Open'], row['High'], row['Low'], row['Close'], row['Volume'], row['Adj Close']) for row in dReader]
	return histPrices
def getHistoricalRates(indexSymbol):
	req = urllib2.urlopen(source+indexSymbol)
	rates = req.read()
	dReader = csv.DictReader(sIO(rates))
	histRates = {}
	for row in dReader:
		histRates[dt.datetime.strptime(row['Date'], dateFormat)] = float(row['Adj Close'])/100.0
	return histRates

def createDateSuffix(day, month, year):
	suff = '&a='
	suff += str(month - 1)
	suff += '&b='
	suff += str(day)
	suff += '&c='
	suff += str(year)
	return suff

def date_range(start, end=dt.date.today()):
	r = (end+dt.timedelta(days=1)-start).days
	return [start+dt.timedelta(days=i) for i in range(r)]


def datetimeIterator(from_date=dt.datetime.now(), to_date=None):
	while to_date is None or from_date <= to_date:
		yield from_date
		from_date = from_date + dt.timedelta(days = 1)
	return


	
	
		
	