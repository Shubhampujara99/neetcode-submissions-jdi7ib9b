class Solution:
    def validPalindrome(self, s: str) -> bool:

        def Pal(L,R):
            isPal = True
            while(L<R):
                if(s[L]==s[R]):
                    L+=1
                    R-=1
                else:
                    isPal = False
                    break
            if(isPal==True):
                return True
            return False

        l,r = 0, len(s)-1
        while(l<r):
            if(s[l] != s[r]):
                return(Pal(l+1,r) or Pal(l,r-1))
            l +=1
            r-=1
        return True


                
