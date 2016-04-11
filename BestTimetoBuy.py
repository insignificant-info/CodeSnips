class Solution(object):
   def maxProfit(self, prices):
       """
       Say you have an array for which the ith element is the price of a given stock on day i.

       If you were only permitted to complete at most one transaction (ie, buy one and sell one 
       share of the stock), design an algorithm to find the maximum profit.

       
       :type prices: List[int]
       :rtype: int
       """
       
       # handle null base cases
       if len(prices) < 2:
            return 0

       best = prices[1] - prices[0]
       low = prices[0]
       
       for price in prices:
           if (price - low) > best:
               best = price - low
               
           if price < low:
               low = price
               
       return best