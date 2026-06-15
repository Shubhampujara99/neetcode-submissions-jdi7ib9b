class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        ls = []
        for num, cnt in count.items():
            ls.append([cnt, num])
        ls.sort()

        ans = []
        while len(ans) < k:
            ans.append(ls.pop()[1])
        return ans