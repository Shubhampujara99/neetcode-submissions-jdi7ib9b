class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        ans = 0
        for R in range(len(s)):
            for L in range(len(g)):
                if(s[R]>= g[L]):
                    g = g[:L] + g[L+1:]
                    ans +=1
                    break
        return ans