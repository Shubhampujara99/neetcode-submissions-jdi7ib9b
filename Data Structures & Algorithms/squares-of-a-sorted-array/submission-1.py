class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = map(lambda x: x ** 2, nums)
        ans = list(squared)
        fans = []
        L,R = 0, len(ans)-1
        while(L<=R):
            if(ans[L]<=ans[R]):
                fans.append(ans[R])
                R-=1
            else:
                fans.append(ans[L])
                L+=1
        return fans[::-1]