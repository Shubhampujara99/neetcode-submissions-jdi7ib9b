class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        space = False
        ans = 0
        for i in range(n-1,-1,-1):
            if(s[i]!=" "):
                while(i>=0 and s[i]!=" "):
                    ans+=1
                    i-=1
                break
            
        return ans