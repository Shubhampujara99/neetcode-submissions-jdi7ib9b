class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        n = len(numbers)
        R = n-1

        while(L<R):
            if(numbers[R] + numbers[L]==target):
                return [L+1,R+1]
            elif(numbers[L] + numbers[R]<target):
                L+=1
            elif(numbers[R] + numbers[L]>target):
                R-=1
