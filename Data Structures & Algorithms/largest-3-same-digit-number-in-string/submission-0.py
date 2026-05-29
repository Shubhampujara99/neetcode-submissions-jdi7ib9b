class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        ans = []
        for i in range(n):
            if(i+2<n and num[i]==num[i+1]==num[i+2]):
                ans.append(num[i])
        
        if(len(ans)==0):
            return ""
        else:
            return max(ans)*3