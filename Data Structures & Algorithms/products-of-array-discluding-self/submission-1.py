class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        num=[]
        for i in range(n):
            L=0
            R=n-1
            prod=1
            while(L<=R):
                if(L==i):
                    L+=1
                elif(R==i):
                    R-=1
                elif(L==R):
                    prod*=nums[L]
                    L+=1
                else:
                    prod *=nums[L]*nums[R]
                    L+=1
                    R-=1
            num.append(prod)
        return num