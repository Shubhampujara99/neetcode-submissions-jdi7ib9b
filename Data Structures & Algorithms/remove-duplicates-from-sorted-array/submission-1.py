class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        L = n-1
        R = n-2

        while(L>0):
            if(nums[L]==nums[R]):
                nums.pop(L)
                L-=1
                R-=1
            else:
                L-=1
                R-=1
        return len(nums)