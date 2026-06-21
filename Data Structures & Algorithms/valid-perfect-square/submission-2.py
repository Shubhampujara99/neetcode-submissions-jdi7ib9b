import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        ans = False
        if(num == 1):
            return True
        root = int(math.sqrt(num) + 1)
        for i in range(root):
            if(i*i==num):
                ans = True
                break
        return ans