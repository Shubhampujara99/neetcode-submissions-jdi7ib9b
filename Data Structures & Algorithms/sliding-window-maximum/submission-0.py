class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        n = len(nums)

        for i in range(n - k + 1):
            maxnum = nums[i]
            for j in range(i, i + k):
                maxnum = max(maxnum, nums[j])
            ans.append(maxnum)

        return ans