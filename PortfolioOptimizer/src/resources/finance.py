'''
Created on Sep 13, 2012

@author: Josh
'''
import numpy as num
import utilities as u
from datetime import date

class Portfolio(object):
    """Represents a portfolio, which consists of a list of assets as well as a start date."""
    
    def __init__(self, assets=[], startdate=date.min, ratemethod="Log"):
        self.assets = assets
        self.startdate = startdate
        self.ratemethod = ratemethod
        
    def addAsset(self, asset):
        self.assets.append(asset)
        
    def getAllocations(self):
        totalstd = 0
        allocations = {}
        for asset in self.assets:
            annstd = asset.getStd(startdate=self.startdate, ratemethod=self.ratemethod, annualized=True)
            totalstd += 1/annstd
        for asset in self.assets:
            annstd = asset.getStd(startdate=self.startdate, ratemethod=self.ratemethod, annualized=True)
            allocations[asset.symbol] = (1/annstd)/totalstd
        return allocations

class Asset:
    """Represents an asset"""
    def __init__(self, symbol, prices):
        self.symbol = symbol
        self.prices = {}
        for p in prices:
            self.prices[p.date] = p
            
        self.startdate = min([date for date,price in self.prices.iteritems()])    
    
    def getVar(self, rates={}, startdate=None, ratemethod="Log", annualized=False):
        if len(rates)==0:
            rates = self.getRatesOfReturn(startdate, ratemethod)
        var = num.var(rates.itervalues())
        if annualized:
            var = var*252
        return var
        
    def getStd(self, rates={}, startdate=None, ratemethod="Log", annualized=False):
        if startdate==None:
            startdate = self.startdate
        if len(rates)==0:
            rates = self.getRatesOfReturn(startdate, ratemethod)
            
        std = num.std(rates.itervalues())
        if annualized:
            std = num.sqrt(252)*std
        return std
     
        
    def getMeanROR(self,rates={},startdate=None, ratemethod="Log", annualized=False):
        if startdate==None:
            startdate = self.startdate
        if len(rates)==0:
            rates = self.getRatesOfReturn(startdate, ratemethod)
        
        meanROR = num.mean(rates.itervalues())
        if annualized:
            meanROR = meanROR*252
        return meanROR
    
    def getBeta(self, startdate=None, method=""):
        pass
    
    def getRatesOfReturn(self, startdate=None, method="Log"):
        if startdate==None:
            startdate = self.startdate
        prices = self.prices
#        prices = [float(prices[date].adjclosing) for date in u.date_range(startdate) if date in prices.keys()]
        
        dates = [d for d in u.date_range(startdate) if d in prices.keys()]
        
        rates = {}
        for i in range(len(dates)):
            if i != 0:    
                d1 = prices[dates[i]].adjclosing
                d2 = prices[dates[i-1]].adjclosing
                if method=="Log":
                    if d1 != 0.00 and d2 != 0.00:
                        rates[dates[i]] = num.log(d1)-num.log(d2)
                elif method=="Simple":
                    if d2 != 0.00:
                        rates[dates[i]] = (d1-d2)/d2
        return rates
    
class AssetPrice:
    """Represents the price of an asset on a given day"""
    
    def __init__(self, date, opening, high, low, closing, volume, adjclosing):
        self.date = date
        self.opening = opening
        self.high = high
        self.low = low
        self.closing = closing
        self.volume = volume
        self.adjclosing = adjclosing