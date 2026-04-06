class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total = 0

        for i in range(n):
            maxL = 0
            maxR = 0

            L = i
            while L >= 0:
                maxL = max(maxL, height[L])
                L -= 1

            R = i
            while R < n:
                maxR = max(maxR, height[R])
                R += 1

            water = min(maxL, maxR) - height[i]
            total += max(0, water)

        return total