import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        n=len(prices)
        low = math.inf
        profit = 0
        while(L<n-1):
            N = L+1
            AN = L+2
            if(N<n and prices[L]<prices[N]):
                low = prices[L]
                while(AN<n and prices[N]<prices[AN] ):
                    N+=1
                    AN+=1
                profit += (prices[N]-low)
                L=N
            else:
                L+=1
        return profit


