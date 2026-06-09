class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        for i in range(n):
            flag = True
            for j in range(n):
                if(i==j):
                    continue 
                if(s[i]==s[j]):
                    flag = False
                    break
            if flag:
                return i
        return -1