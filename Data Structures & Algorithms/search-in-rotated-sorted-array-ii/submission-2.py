class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        L=0
        n = len(nums)
        R = n-1
        while(L<=R):
            mid = (L+R)//2
            if(target==nums[mid]):
                return True
            elif nums[L] == target:
                return True
            elif nums[R] == target:
                return True
            elif nums[L] < nums[mid]:
                if nums[L] <= target < nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
            elif(nums[L]>nums[mid]):
                if nums[mid] < target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1
            else:
                L+=1
        return False