class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            small = nums[i]
            for j in range(i+1,len(nums)):
                if(nums[j]<small):
                    temp = small
                    small = nums[j]
                    nums[j] = temp
                else:
                    continue
            nums[i] = small
        return nums
