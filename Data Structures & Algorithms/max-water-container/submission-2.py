class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        n = len(heights)
        max_area = 0
        for l in range(n):
            r= n-1
            while(l<r):
                width = r-l
                height = min(heights[l],heights[r])
                area = width*height
                if(area>max_area):
                    max_area = area
                r-=1
        return max_area

        