class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count=0
        ans = []
        ans2 = []
        ans3 = []
        for i in s:
            if(i=="1"):
                count+=1
            else:
                ans.append(0)
                
        for i in range(count-1):
            ans2.append(1)
        ans.append(1)
        ans2 = ans2 + ans
        ans3 = ''.join(str(x) for x in ans2)
        return ans3

        