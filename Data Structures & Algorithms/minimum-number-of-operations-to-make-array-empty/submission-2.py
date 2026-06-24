class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        print(freq)

        count = 0
        for key,value in freq.items():
            if(value==1):
                return -1
            else:
                count += (value + 2) // 3
        return count