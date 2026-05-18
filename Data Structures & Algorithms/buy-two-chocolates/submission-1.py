import math
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = math.inf
        min2 = math.inf
        for i in prices:
            if(i<min1):
                min2 = min1
                min1 = i
            elif(i<min2):
                min2 = i
        if(money - min1 - min2>=0):
            return money - min1 - min2
        else:
            return money
            