class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n1 = len(nums) 
        n2 = len(nums)//3
        ans = []
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        # print(freq)
        
        for i in range(len(freq)):
            if(list(freq.values())[i]>n2):
                ans.append(list(freq.keys())[i])
        return ans