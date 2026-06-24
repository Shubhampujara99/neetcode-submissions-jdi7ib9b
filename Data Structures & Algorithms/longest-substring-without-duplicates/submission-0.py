class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        n = len(s)
        ans= 0
        for L in range(n):
            nset = set()
            for R in range(L,n):
                if(s[R] in nset):
                    break
                nset.add(s[R])
            ans = max(ans, len(nset))
        return ans