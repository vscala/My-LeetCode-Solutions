class Solution:
    def numTrees(self, n: int) -> int:
        # catalan numbers 
        
        @cache
        def count(n):
            if n == 0 or n == 1: return 1
            
            out = 0
            for i in range(n):
                out += count(i) * count(n-i-1)
            return out
        return count(n)