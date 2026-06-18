class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = [str(n) for n in nums]

        ans = []
        while arr:
            maxi = 0
            for i in range(1, len(arr)):
                if arr[i] + arr[maxi] > arr[maxi] + arr[i]:
                    maxi = i
            ans.append(arr[maxi])
            arr.pop(maxi)

        ansult = "".join(ans)
        return ansult if ansult[0] != '0' else '0'