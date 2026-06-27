class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        ans = 100
        for i in range(n):
            cb = 0
            cw = 0
            if(blocks[i]=="W"):
                cw+=1
            else:
                cb+=1
            if(cb + cw) == k:
                ans = min(ans, cw)
            for j in range(i+1,n):
                    if(blocks[j]=="W"):
                        cw +=1
                    else:
                        cb +=1
                    if(cb+cw==k):
                        ans = min(ans,cw)
        if(ans==100):
            return 0
        return ans
                    