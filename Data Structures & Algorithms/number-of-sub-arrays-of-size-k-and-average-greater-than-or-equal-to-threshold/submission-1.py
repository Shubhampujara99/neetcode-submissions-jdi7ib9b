class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        count = 0
        lm = n-k+1
        for i in range(lm):
            sums = arr[i]
            for j in range(i+1,i+k):
                sums += arr[j]
            print(sums)
            avg = sums/k
            if(avg>=threshold):
                count +=1
        return count