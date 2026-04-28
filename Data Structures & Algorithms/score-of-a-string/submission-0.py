class Solution:
    def scoreOfString(self, s: str) -> int:
        L = 0
        n = len(s)
        ans = 0
        for R in range(L+1,n):
            ans = ans + abs(ord(s[L]) - ord(s[R]))
            L+=1
        return ans