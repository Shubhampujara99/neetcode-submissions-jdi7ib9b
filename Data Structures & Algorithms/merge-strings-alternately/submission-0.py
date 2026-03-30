class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        L1 = 0
        L2 = 0
        n1 = len(word1)
        n2 = len(word2)
        ans = ""
        while (L1 < n1 or L2 < n2):
            if (L1 < n1):
                ans += word1[L1]
                L1 += 1
            if (L2 < n2):
                ans += word2[L2]
                L2 += 1
        return ans
            