class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ind = 0
        for i in range(len(arr)):
            if(abs(x-arr[ind])>abs(x-arr[i])):
                ind = i
        res = [arr[ind]]
        L = ind-1
        R = ind+1
        n = len(arr)
        while(len(res)<k):
            if(L>=0 and R<n):
                if abs(x - arr[L]) <= abs(x - arr[R]):
                    res.append(arr[L])
                    L -= 1
                else:
                    res.append(arr[R])
                    R += 1
            elif L >= 0:
                res.append(arr[L])
                L -= 1
            elif R < n:
                res.append(arr[R])
                R += 1

        return sorted(res)