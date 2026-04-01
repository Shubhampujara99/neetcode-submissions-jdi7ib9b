class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i=0
        j=0
        r = n-1
        while(i<k):
                nums[:] = [nums[-1]] + nums[0:-1]
                i+=1