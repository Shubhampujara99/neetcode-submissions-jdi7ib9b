class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        L = 0
        n = len(nums)
        ans = 0
        temp = []
        while(L<n):
            if(nums[L]==1):
                ans+=1
            if(nums[L]==0):
                temp.append(ans)
                ans = 0
            L+=1
        temp.append(ans)
        return max(temp)

                
