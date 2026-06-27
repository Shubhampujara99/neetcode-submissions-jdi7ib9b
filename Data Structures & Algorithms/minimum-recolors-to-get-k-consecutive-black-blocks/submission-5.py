class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        L = 0
        count = 0
        least = n+1
        for R in range(n):
            if(blocks[R]=="W"):
                count +=1
            if(R-L+1>k):
                if blocks[L] == "W":
                    count -= 1
                L += 1
            if(R-L+1==k):
                least = min(least,count)
        return least