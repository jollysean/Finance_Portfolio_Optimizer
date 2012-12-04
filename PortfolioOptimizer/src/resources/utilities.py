import csv
import urllib2
import json
import finance as fin
import datetime as dt
import sys
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
		histRates[dt.datetime.strptime(row['Date'], dateFormat).date()] = (float(row['Adj Close'])/100.0)/365
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

def optimizePortfolio(portfolio, numSamples = 1, minRetRate = None):
	resultList = []
	lowerMin = sys.float_info.max
	upperMin = sys.float_info.min
	for asset in portfolio.assets:
		assMean = asset.getMeanROR()
		if assMean < lowerMin:
			lowerMin = assMean
		if assMean > upperMin:
			upperMin = assMean
	
	mincrease = (upperMin - lowerMin)/numSamples
	minReturn = lowerMin
	if numSamples == 1 and minRetRate != None:
		minReturn = minRetRate
		
	for n in range(numSamples):
		minReturn += n*mincrease
			
		url = "http://optimization.andrewgaspar.com/api/optimize"
		data = {'MinimumReturn': minReturn, 'Stocks' : [] }
		headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'}
		assets = portfolio.assets
		for i in range(len(assets)):
			stock = {'Symbol': assets[i].symbol, 'MeanReturnRate': assets[i].getMeanROR(), 'Covariances': {}}
			for j in range(len(assets)):
				stock['Covariances'][assets[j].symbol] = portfolio.cvmatrix[i][j]
			data['Stocks'].append(stock)
		
		request = urllib2.Request(url, json.dumps(data), headers)
		resp = urllib2.urlopen(request)
		optResult = json.loads(resp.read())
		resultList.append(optResult)
	
	return resultList
	
	
		
	