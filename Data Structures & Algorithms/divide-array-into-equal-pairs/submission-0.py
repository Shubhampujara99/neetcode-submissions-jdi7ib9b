class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = len(nums)
        if(n%2 !=0):
            return False
        nums.sort()
        L = 0
        R = 1
        while(R<n):
            if(nums[L]!=nums[R]):
                return False
            L+=2
            R+=2

        return True