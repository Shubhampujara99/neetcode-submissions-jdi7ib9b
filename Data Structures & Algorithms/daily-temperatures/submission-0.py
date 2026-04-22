class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        L = 0
        result = []
        n = len(temperatures)
        while(L<n):
            i = 1
            found = False
            for R in range(L+1,n):
                if(temperatures[R]>temperatures[L]):
                    result.append(i)
                    found = True
                    break
                else:
                    i+=1
            if not found:
                result.append(0)
            L+=1
        return result