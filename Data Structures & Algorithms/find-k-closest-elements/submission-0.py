class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        L = 0
        n = len(arr)
        R = n-1
        while(R-L+1> k):            
                if(abs(x-arr[L]) <= abs(x-arr[R])):
                    R-=1
                elif(abs(x-arr[L])>abs(x-arr[R])):
                    L+=1
        return arr[L:R+1]