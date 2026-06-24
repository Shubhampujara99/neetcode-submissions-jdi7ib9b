import math
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num > 0:
                s.add(num)
        ans = 1
        while ans in s:
            ans += 1
        return ans
            