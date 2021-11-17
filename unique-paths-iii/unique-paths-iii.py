class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        out = 0
        start = None
        zeros = 0
        for i, r in enumerate(grid):
            for j, v in enumerate(r):
                if v == 0: zeros += 1
                elif v == 1: start = ((i, j))
        
        q = [[start]]
        while q:
            path = q.pop(0)
            i, j = path[-1]
            
            if grid[i][j] == 2:
                if len(path) == zeros+2: 
                    out += 1
            elif grid[i][j] != -1:
                if i > 0 and (i-1, j) not in path:
                    q.append(path[:] + [(i-1, j)])
                if j > 0 and (i, j-1) not in path:
                    q.append(path[:] + [(i, j-1)])
                if i < len(grid) - 1 and (i+1, j) not in path:
                    q.append(path[:] + [(i+1, j)])
                if j < len(grid[0]) - 1 and (i, j+1) not in path:
                    q.append(path[:] + [(i, j+1)])
        return out
                    
                
            
            
            
            
            