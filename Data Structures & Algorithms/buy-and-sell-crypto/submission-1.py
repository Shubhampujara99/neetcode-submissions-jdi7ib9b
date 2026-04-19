class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        R = 1
        n = len(prices)
        profit = 0
        while(R<n):
            if(prices[R]>prices[L]):
                profit = max(prices[R]-prices[L],profit)
                R+=1
            else:
                L=R
                R+=1
        return profit
            