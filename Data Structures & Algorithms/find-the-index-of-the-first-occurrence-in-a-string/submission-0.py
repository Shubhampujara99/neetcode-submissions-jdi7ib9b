class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for start in range(len(haystack) - len(needle) + 1):
            R = 0

            for L in range(start, start + len(needle)):
                if haystack[L] == needle[R]:
                    R += 1
                else:
                    break

            if R == len(needle):
                return start

        return -1