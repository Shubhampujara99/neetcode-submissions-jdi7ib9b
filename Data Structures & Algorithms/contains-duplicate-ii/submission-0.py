class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = 0
        n = len(nums)
        ans = 0
        for L in range(n):
            for R in range(L+1, min(n,L+k+1)):
                if(nums[L]==nums[R]):
                    return True
                R+=1
        return False
        