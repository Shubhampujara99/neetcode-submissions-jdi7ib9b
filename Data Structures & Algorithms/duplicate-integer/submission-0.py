class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num2 = set(nums)
        if (len(num2) != len(nums)):
            return True
        else:
            return False