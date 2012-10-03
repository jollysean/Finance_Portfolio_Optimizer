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
			
def createDateSuffix(day, month, year):
	suff = '&a='
	suff += str(month - 1)
	suff += '&b='
	suff += str(day)
	suff += '&c='
	suff += str(year)
	return suff




	
	
		
	