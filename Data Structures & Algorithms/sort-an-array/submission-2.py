class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            small = i
            for j in range(i+1,len(nums)):
                if(nums[j]<nums[small]):
                    small = j
                else:
                    continue
            nums[i], nums[small] = nums[small], nums[i]

        return nums
