class Solution:
    def firstUniqChar(self, s: str) -> int:
        sets = defaultdict(int)
        for i in s:
            sets[i] += 1
        
        for i,j in enumerate(s):
            if (sets[j] ==1):
                return i
        return -1