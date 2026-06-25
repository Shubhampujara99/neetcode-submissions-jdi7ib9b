class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0
        total = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1:
                    land_neighbors = 0
                    
                    for dr, dc in directions:
                        ni, nj = i + dr, j + dc
                        
                        if 0 <= ni < num_rows and 0 <= nj < num_cols:
                            if grid[ni][nj] == 1:
                                land_neighbors += 1
                    count += land_neighbors
                    total +=1
        ans = 4*total - count
        return ans

