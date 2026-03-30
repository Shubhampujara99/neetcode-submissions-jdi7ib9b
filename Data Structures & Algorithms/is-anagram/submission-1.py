class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lists = []
        listt = []

        for ch in s:
            lists.append(ch)
        for ch in t:
            listt.append(ch)

        for ch in lists:
            found = False
            for chs in listt:
                if ch == chs:
                    listt.remove(chs)
                    found = True
                    break
            if not found:
                return False
        
        if(len(listt)==0):
            return True
        return False
                
