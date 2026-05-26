class Solution:
        def maxDepth(self, s: str) -> int:
            ans = 0
            L = 0
            n = len(s)
            R = 0

            for R in range(n):
                if(s[R] == "("):
                    L += 1
                    ans = max(L, ans)

                elif(s[R] == ")"):
                    L -= 1

            return ans