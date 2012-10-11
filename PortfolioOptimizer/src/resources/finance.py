'''
Created on Sep 13, 2012

@author: Josh
'''
import numpy as num
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
            annstd = asset.getStd(self.startdate, self.ratemethod, True)
            totalstd += 1/annstd
        for asset in self.assets:
            annstd = asset.getStd(self.startdate, self.ratemethod, True)
            allocations[asset.symbol] = (1/annstd)/totalstd
        return allocations

class Asset:
    """Represents an asset"""
    def __init__(self, symbol, prices):
        self.symbol = symbol
        self.prices = prices
        self.startdate = min([p.date for p in self.prices])
        self.rates = self.getRatesOfReturn()
        
    def getMeanVarStd(self, annualized=False):
        mean = num.mean(self.rates)
        variance = num.var(self.rates)
        std = num.std(self.rates)
        if annualized:
            return (252*mean, 252*variance, num.sqrt(252)*std)
        else:
            return (mean, variance, std)
    
    def getVar(self, startdate=None, method="Log", annualized=False):
        rates = self.getRatesOfReturn(startdate, method)
        var = num.var(rates)
        if annualized:
            var = var*252
        return var
        
    def getStd(self, startdate=None, method="Log", annualized=False):
        if startdate==None:
            startdate = self.startdate
        
        rates = self.getRatesOfReturn(startdate, method)
        std = num.std(rates)
        if annualized:
            std = num.sqrt(252)*std
        return std
     
        
    def getMeanROR(self,startdate=None, method="Log", annualized=False):
        if startdate==None:
            startdate = self.startdate
        
        rates = self.getRatesOfReturn(startdate, method)
        meanROR = num.mean(rates)
        if annualized:
            meanROR = meanROR*252
        return meanROR
    
    
    def getRatesOfReturn(self, startdate=None, method="Log"):
        if startdate==None:
            startdate = self.startdate
        prices = self.prices
        prices = [float(price.adjclosing) for price in prices if price.date >= startdate]
        prices.reverse()
        rates = []
        for i in range(len(prices)):
            if i != 0:
                d1 = prices[i]
                d2 = prices[i-1]
                if method=="Log":
                    if d1 != 0.00 and d2 != 0.00:
                        rates.append(num.log(d1)-num.log(d2))
                elif method=="Simple":
                    if d2 != 0.00:
                        rates.append((d1-d2)/d2)
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