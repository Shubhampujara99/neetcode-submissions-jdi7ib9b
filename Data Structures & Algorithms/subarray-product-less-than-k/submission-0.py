class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        L = 0
        res = 1
        for R in range(n):
            res *= nums[R]
            while(res>=k and L<=R):
                res //= nums[L] 
                L +=1
            count+= R-L+1
        return count