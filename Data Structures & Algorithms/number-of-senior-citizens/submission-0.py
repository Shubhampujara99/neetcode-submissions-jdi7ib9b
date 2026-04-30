class Solution:
    def countSeniors(self, details: List[str]) -> int:
        age= [w[-4:-2] for w in details]
        ans = 0
        for i in range(len(age)):
            if(int(age[i])>60):
                ans+=1
        return ans
