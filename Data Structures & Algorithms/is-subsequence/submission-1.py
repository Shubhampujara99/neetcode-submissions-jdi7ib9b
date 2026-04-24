class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        L = 0
        R = 0
        n1 = len(s)
        n2 = len(t)
        while(L<n1 and R<n2):
            if(s[L]==t[R]):
                L+=1
                R+=1
            else:
                R+=1
                if(R==n2):
                    return False
        return L==n1
