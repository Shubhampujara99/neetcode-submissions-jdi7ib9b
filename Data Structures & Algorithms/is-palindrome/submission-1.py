import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs = re.sub(r'[^a-zA-Z0-9]', '', s)
        cs = cs.lower()
        L = 0
        n = len(cs)
        R = n-1
        while (L<R):
            if(cs[L]==cs[R]):
                R-=1
                L+=1
            else:
                    return False
        return True
        
