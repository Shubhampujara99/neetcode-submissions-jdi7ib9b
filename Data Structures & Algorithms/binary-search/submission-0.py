class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        L=0
        R=n-1
        while(L<=R):
            mid = (L+R)//2
            if(target>nums[mid]):
                L=mid+1
            elif(target<nums[mid]):
                R=mid-1
            else:
                return mid
        return -1