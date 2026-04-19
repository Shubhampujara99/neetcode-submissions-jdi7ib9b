class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        profit = 0
        for L in range(len(prices)):
            for R in range(L+1,len(prices)):
                if(prices[R]-prices[L]>profit):
                    profit = prices[R]-prices[L]
        return profit