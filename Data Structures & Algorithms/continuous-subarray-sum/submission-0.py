class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
            for i in range(len(nums) - 1):
                sums = nums[i]
                for j in range(i + 1, len(nums)):
                    sums += nums[j]
                    if sums % k == 0:
                        return True
            return False