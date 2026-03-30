class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        lists = []
        for i in range(len(nums)):
            if nums[i] == val:
                lists.append(i)

        for j in reversed(lists):
            nums.pop(j)

        return len(nums)