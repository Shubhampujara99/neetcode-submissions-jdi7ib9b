class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        L = 0
        R = len(nums) - 1
        while(L<=R):
            if(nums[L]%2!=0):
                nums[L],nums[R] = nums[R], nums[L]
                R-=1
            else:
                L+=1
        return nums