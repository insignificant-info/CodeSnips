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
           
       # find the max differential 
       # Initialize the best_increase to something very negative (this could be done better)
       best_increase = -999
       #Iterate through all first prices
       # for i,first_price in enumerate(prices[:-1]):
       #      # Skip the very last number in prices from consideration
       #      #if i != (len(prices) - 1) :
       #      #Check all first prices against all second prices
       #      for j,second_price in enumerate(prices[i+1:]):
       #          best_increase = max(second_price - first_price, best_increase)

       # Find Global Minima and Maxima 
       (max_val,min_val) = self.find_extremes(prices)

       # if the global maxima occurs after the global minima, we're done.
       if min_val['location'] < max_val['location']:
            return max_val['value'] - min_val['value']
       else:
            (A_max_val,A_min_val) = self.find_extremes(prices[:max_val['location']+1])
            (B_max_val,B_min_val) = self.find_extremes(prices[min_val['location']:])
            A_value = A_max_val['value'] - A_min_val['value']
            B_value = B_max_val['value'] - B_min_val['value']
            return A_value if A_value>B_value else B_value

   def find_extremes(self, prices):
   #def find_extremes(prices):
      """
      Pass in a slice (or all) of prices and find the extreme max and min as well as their locations

      Input:
      prices - A list of sequential prices (slice as needed)

      Returns:
      max_val, min_val - Dicts with keys value and location


      *** What's the self for?, is it needed?


      """

      max_val = {"value" : -999999999, "location" : 0}
      min_val = {"value" : +999999999, "location" : 0}

      for i,price in enumerate(prices):
            if price > max_val['value']:
                  max_val['value'] = price
                  max_val['location'] = i
            if price < min_val['value']:
                  min_val['value'] = price
                  min_val['location'] = i

      return max_val, min_val





                    
