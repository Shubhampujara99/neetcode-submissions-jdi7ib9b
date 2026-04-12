class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L=0
        n = len(nums)
        num=[]
        while(L<n):
            prod=1
            R=0
            while(R<n):
                if(L!=R):
                    prod *=nums[R]
                    R+=1
                else: R+=1
            num.append(prod)
            L+=1
        return num
