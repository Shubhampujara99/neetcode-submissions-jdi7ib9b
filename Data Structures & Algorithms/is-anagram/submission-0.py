class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lists = []
        listt = []

        for ch in s:
            lists.append(ch)
        lists.sort()
        
        for ch in t:
            listt.append(ch)
        listt.sort()

        if (lists == listt):
            return True
        return False