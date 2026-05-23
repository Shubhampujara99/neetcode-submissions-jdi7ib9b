class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for L in range(n-1):
            for R in range(L+1,n):
                if(nums[L]==nums[R]):
                    count+=1
        return count