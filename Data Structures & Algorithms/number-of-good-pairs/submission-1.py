class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        counts = {item: nums.count(item) for item in set(nums)}
        ans = 0

        for i in counts.values():
            if(i > 1):
                ans += sum(j for j in range(i))
    
        return ans