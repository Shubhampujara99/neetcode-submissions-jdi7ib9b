import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs = re.sub(r'[^a-zA-Z0-9]', '', s)
        cs = cs.lower()
        rcs = "".join(reversed(cs))
        if(rcs == cs):
            return True
        return False
