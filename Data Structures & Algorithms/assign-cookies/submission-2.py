class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)

        R,L = 0,0
        while L<len(g) and R<len(s):
            if(s[R]>=g[L]):
                L+=1
            R+=1
        return L