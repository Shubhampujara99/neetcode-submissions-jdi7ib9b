class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        L = 0
        n= len(arr)
        while(L<n):
            ans = 0
            for R in range(L+1,n):
               if(arr[R]>ans):
                ans = arr[R]
            arr[L]=ans
            if(L==n-1):
                arr[L] = -1
            L+=1
        return arr