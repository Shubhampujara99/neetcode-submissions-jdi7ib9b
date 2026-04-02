class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        n = len(heights)
        max_area = 0
        r= n-1
        while(l<r):
            width = r-l
            height = min(heights[l],heights[r])
            area = width*height
            if(area>max_area):
                max_area = area
            if(heights[l]>heights[r]):
                r-=1
            elif(heights[l]<=heights[r]):
                l+=1
        return max_area

        