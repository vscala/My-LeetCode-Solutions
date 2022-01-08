class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @cache
        def maxCherries(i, j1, j2):
            if j1 > j2: return maxCherries(i, j2, j1) # optimization by symmetry
            if i == len(grid) or j1 == -1 or j2 == len(grid[0]): return 0
            
            out = 0
            for d1 in range(-1, 2):
                for d2 in range(-1, 2):
                    out = max(out, maxCherries(i+1, j1+d1, j2+d2))
            return out + (grid[i][j1] + grid[i][j2]) if j1 != j2 else (grid[i][j1])
        return maxCherries(0, 0, len(grid[0])-1)