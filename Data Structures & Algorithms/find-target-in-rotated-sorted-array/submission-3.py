class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L=0
        n = len(nums)
        R = n-1
        while(L<=R):
            mid = (L+R)//2
            if(target==nums[mid]):
                return mid
            elif nums[L] == target:
                return L
            elif nums[R] == target:
                return R
            elif nums[L] <= nums[mid]:
                if nums[L] <= target < nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
            else:
                if nums[mid] < target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1
        return -1
