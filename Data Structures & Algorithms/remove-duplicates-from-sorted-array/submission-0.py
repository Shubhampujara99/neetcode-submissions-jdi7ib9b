class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        un = sorted(set(nums))
        nums[:len(un)] = un
        return len(un)