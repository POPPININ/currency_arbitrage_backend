from .EdgeWeightedDigraph import EdgeWeightedDigraph
from .BellmanFordSP import BellmanFordSP
from .WDE import WDE
from math import log, exp

class Arbitrage:

    def __init__(self, exchRates : dict, currencyNames : list):
        self.V = len(exchRates)
        self.G = EdgeWeightedDigraph(self.V)
        self.conversions = []

        # create network of currencies
        for currency, rates in exchRates.items():
            rateList = rates # list of exchange rates
            v = int(currency)
            for w in range(len(rateList)):
                rate = rateList[w]
                e = WDE(v, w, -log(rate))
                self.G.addEdge(e)
        
        self.spt = BellmanFordSP(self.G, 0)
        self.spt.initializeSPsearch()

        if self.spt.hasNegativeCycle():
            stake = 1000.0
            for e in self.spt.negativeCycle():
                self.conversions.append(currencyNames[e.From()])
                self.conversions.append('->')
                self.conversions.append(currencyNames[e.To()])
                # print(currencyNames[e.From()], '->', currencyNames[e.To()])
                # stake *= exp(-e.weight)
        # else:
            # print('No arbitrage opportunity found.')
            
exchRates = { 0 : [1, 1.16],
              1 : [0.95, 1] }

currencyNames = ['EUR', 'USD']



                
        

