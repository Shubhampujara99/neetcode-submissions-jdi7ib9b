class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n+1

        for i in range(n):
            sums = nums[i]
            j = i+1
            if(sums>=target):
                ans = min(ans,1)
            while(sums<target and j<n):
                sums +=nums[j]
                j +=1
                if(sums>=target):
                    ans = min(ans,j-i)
        if(ans==n+1):
            return 0
        return ans