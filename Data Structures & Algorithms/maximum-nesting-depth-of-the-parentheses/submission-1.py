class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        stack = []

        for i in s:
            if(i == "("):
                stack.append(i)
                ans = max(ans, len(stack))

            elif(i == ")"):
                stack.pop()

        return ans