class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        L = 0
        R = 0
        n1 = len(s)
        n2 = len(t)
        while(L<n1 and R<n2):
            if(s[L]==t[R]):
                R+=1
            L+=1
        return n2 - R