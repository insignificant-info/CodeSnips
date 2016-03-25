class Solution(object):
   def maxProfit(self, prices):
       """
       Say you have an array for which the ith element is the price of a given stock on day i.

       If you were only permitted to complete at most one transaction (ie, buy one and sell one 
       share of the stock), design an algorithm to find the maximum profit.
       
       Algorithm:
       
       Find a sequence of indecies that results in the greatest profit. That is, we need to find
       a buy point prior to a sell point that maximizes profit.
       
       To do this, we need to find the longest sequence of cumulative sums that's greater tha
       
       :type prices: List[int]
       :rtype: int
       """
       
       # initialize buying and selling indecies
       buyindex = 0
       sellindex = 0
       
       # initialize a list of prices to zero that of size len(prices) -1
       pricedelta = [0 for ii in xrange(len(prices)-1)]
       
       # calculate the first order differential of the prices (did they go up or down)
       for ii in xrange(len(prices)-1):
           pricedelta[ii] = prices[ii+1] - prices[ii]
           
       #