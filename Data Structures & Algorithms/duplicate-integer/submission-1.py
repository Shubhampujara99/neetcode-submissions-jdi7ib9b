class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        ans = True
        for i in range(n):
            for j in range(i+1,n):
                if(nums[j]==nums[i]):
                    return ans
        return not ans