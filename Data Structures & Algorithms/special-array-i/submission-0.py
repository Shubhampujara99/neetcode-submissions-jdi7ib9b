class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        if(n<=1):
            return True
        L = 0
        for R in range(L+1,n):
            n1 = nums[L]%2
            n2 = nums[R]%2
            if(n1==n2):
                return False
            L+=1
        return True