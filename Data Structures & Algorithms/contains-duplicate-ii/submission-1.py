class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        count = set()
        L = 0
        for R in range(n):
            if(R-L>k):
                count.remove(nums[L])
                L+=1
            if(nums[R] in count):
                return True
            count.add(nums[R])
        return False