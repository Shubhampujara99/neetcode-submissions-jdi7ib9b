class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        count = 0
        for i in range(n-1,-1,-1):
            if(nums[i]==0):
                count+=1
                nums.pop(i)
        for i in range(count):
            nums.append(0)
        