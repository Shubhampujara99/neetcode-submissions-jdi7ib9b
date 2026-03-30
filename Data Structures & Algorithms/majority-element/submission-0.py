class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for ele in nums:
            count[ele] +=1;

        for k, v in count.items():
            if v > len(nums) // 2:
                return k
