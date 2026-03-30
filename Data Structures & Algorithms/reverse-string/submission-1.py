class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        cp = []
        for L in s:
            cp.append(L)
        i = 0
        while cp:
            s[i] = cp.pop()
            i+=1