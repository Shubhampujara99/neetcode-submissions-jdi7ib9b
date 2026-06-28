class Solution:
    def atMost(self, nums, goal):
        if goal < 0:
            return 0

        L = 0
        count1 = 0
        ans = 0

        for R in range(len(nums)):
            count1 += nums[R]

            while count1 > goal:
                count1 -= nums[L]
                L += 1

            ans += R - L + 1

        return ans
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.atMost(nums, goal) - self.atMost(nums, goal - 1)
