class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = set()
        for i in nums:
            if i in counts:
                return i
            counts.add(i)
        return -1