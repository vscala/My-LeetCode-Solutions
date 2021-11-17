class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        #i=0 diagonal start
        for i, _ in enumerate(mat[0]):
            stack, n = [], min(len(mat[0]) - i, len(mat))
            for ii in range(n):
                stack += [mat[ii][ii + i]]
            stack.sort()
            for ii in range(n):
                mat[ii][ii + i] = stack[ii]
            
        #j=0 i!=0 diagonal start
        for j in range(1, len(mat)):
            stack, n = [], min(len(mat) - j, len(mat[0]))
            for jj in range(n):
                stack += [mat[jj+j][jj]]
            stack.sort()
            for jj in range(n):
                mat[jj+j][jj] = stack[jj]
        
        return mat