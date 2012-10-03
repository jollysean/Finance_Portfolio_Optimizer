'''
Created on Sep 13, 2012

@author: Josh
'''
import numpy as num
from datetime import date

class Portfolio(object):
    """Represents a portfolio, which consists of a list of assets as well as a start date."""
    
    def __init__(self, assets=None, startdate=None):
        self.assets = assets if assets else []
        self.startdate = startdate if startdate else date.min
        
    def addAsset(self, asset):
        self.assets.append(asset)
        
    def getAllocations(self):
        totalstd = 0
        allocations = {}
        for asset in self.assets:
            (annmean, annvar, annstd) = asset.getMeanVarStd(True)
            totalstd += 1/annstd
        for asset in self.assets:
            (annmean, annvar, annstd) = asset.getMeanVarStd(True)
            allocations[asset.symbol] = (1/annstd)/totalstd
        return allocations

class Asset:
    """Represents an asset"""
    def __init__(self, symbol, prices):
        self.symbol = symbol
        self.prices = prices
        self.startdate = min([p.date for p in self.prices])
        self.rates = self.getRatesOfReturn()
        #(self.mean, self.var, self.std) = u.getMeanVarStd(self.prices)
        #(self.annmean, self.annvar, self.annstd) = u.getMeanVarStd(self.prices, True)
    
    def getMeanVarStd(self, annualized=False):
        mean = num.mean(self.rates)
        variance = num.var(self.rates)
        std = num.std(self.rates)
        if annualized:
            return (252*mean, 252*variance, num.sqrt(252)*std)
        else:
            return (mean, variance, std)
        
    def getRatesOfReturn(self, startdate=None):
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
                if d1 != 0.00 and d2 != 0.00:
                    rates.append(num.log(d1)-num.log(d2))
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