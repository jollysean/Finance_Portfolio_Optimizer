from StringIO import StringIO as sIO
import csv
import datetime as dt
import finance as fin
import json
import sys
import urllib2
from operator import itemgetter

	
	
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

def readStocksFromFile(stockCount, markIndex, sortBy, reverse):
	if markIndex=="SP":
		f = open("S&P500.csv")
	else:
		f = open("DOW30.csv")
		
	vals = f.read()
	dReader = csv.DictReader(sIO(vals))
	stocks = [(row['Symbol'], row[sortBy]) for row in dReader]
	stocks = sorted(stocks, key=itemgetter(1), reverse=reverse)
	if stockCount < len(stocks):
		return stocks[:stockCount]
	else:
		return stocks
	

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

def optimizePortfolio(portfolio, step = 0.0025):
	resultList = []
	
	url = "http://optimization.andrewgaspar.com/api/optimize"
	data = {'Stocks' : [] }
	headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'}
	assets = portfolio.assets
	for i in range(len(assets)):
		stock = {'Symbol': assets[i].symbol, 'MeanReturnRate': assets[i].mean*252, 'Covariances': {}}
		for j in range(len(assets)):
			stock['Covariances'][assets[j].symbol] = portfolio.cvmatrix[i][j]
		data['Stocks'].append(stock)
	
	request = urllib2.Request(url, json.dumps(data), headers)
	resp = urllib2.urlopen(request)
	optResult = json.loads(resp.read())
	
	minReturn = optResult['ExpectedReturn']
	
	resultList.append(optResult)
	
	while True:
		minReturn += step
		data = {'MinimumReturn': minReturn, 'Stocks' : [] }
		headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'}
		assets = portfolio.assets
		for i in range(len(assets)):
			"""I CHANGED IT TO GET THE MEAN RATE OF RETURN FROM assets[i].getMeanROR() RATHER THAN assets[i].annmean"""
			stock = {'Symbol': assets[i].symbol, 'MeanReturnRate': assets[i].mean*252, 'Covariances': {}}
			for j in range(len(assets)):
				stock['Covariances'][assets[j].symbol] = portfolio.cvmatrix[i][j]
			data['Stocks'].append(stock)
			
		request = urllib2.Request(url, json.dumps(data), headers)
		resp = urllib2.urlopen(request)
		optResult = json.loads(resp.read())
		if optResult['Feasible'] == True:
			resultList.append(optResult)
		else:
			break
				
	return resultList

def efficientFrontier(portfolio, step = 0.0001):
	url = "http://optimization.andrewgaspar.com/api/optimize"
	data = {'Stocks' : [] }
	headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'}
	assets = portfolio.assets
	for i in range(len(assets)):
		stock = {'Symbol': assets[i].symbol, 'MeanReturnRate': assets[i].mean*252, 'Covariances': {}}
		for j in range(len(assets)):
			stock['Covariances'][assets[j].symbol] = portfolio.cvmatrix[i][j]
		data['Stocks'].append(stock)
	
	request = urllib2.Request(url, json.dumps(data), headers)
	resp = urllib2.urlopen(request)
	optResult = json.loads(resp.read())
	
	minReturnRate = optResult['ExpectedReturn']

	url = "http://optimization.andrewgaspar.com/api/frontier"
	data = {'Step': step, 'MinimumReturn': minReturnRate, 'Stocks' : [] }
	headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'}
	assets = portfolio.assets
	for i in range(len(assets)):
		stock = {'Symbol': assets[i].symbol, 'MeanReturnRate': assets[i].mean*252, 'Covariances': {}}
		for j in range(len(assets)):
			stock['Covariances'][assets[j].symbol] = portfolio.cvmatrix[i][j]
		data['Stocks'].append(stock)
	
	request = urllib2.Request(url, json.dumps(data), headers)
	resp = urllib2.urlopen(request)
	optResultList = json.loads(resp.read())
	return optResultList
	