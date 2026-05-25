class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 0
        if(n==1):
            return 1
        for i in range(1,n):
            if(i<n):
                n -= i
                ans +=1
            else:
                break
        return ans