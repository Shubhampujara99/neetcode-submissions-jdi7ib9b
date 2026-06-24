class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans = 1
        nums.sort()
        for i in range(len(nums)):
            if(nums[i]>-1):
                if(nums[i]==ans):
                    ans+=1
        return ans