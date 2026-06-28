class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        sums = 0
        n = len(nums)
        ans = n+1
        for R in range(n):
            sums += nums[R]

            while sums >= target:
                ans = min(ans, R-L+1)
                sums -= nums[L]
                L += 1
        if(ans==n+1):
            return 0
        return ans