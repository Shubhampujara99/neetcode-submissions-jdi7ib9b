class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        val = []
        for i in grid:
            for j in i:
               val.append(j) 
        val = sorted(val)
        
        n2 = len(val)
        repeated = sum(val) - sum(set(val))

        ideal_sum = n2 * (n2 + 1) // 2
        missing = ideal_sum - sum(set(val))

        ans = []
        ans.append(repeated)
        ans.append(missing)  
        return ans    