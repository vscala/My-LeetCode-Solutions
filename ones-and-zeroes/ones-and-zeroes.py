class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        strs.sort(key=len)
        ones  = [s.count("1") for s in strs]
        zeros = [len(strs[i]) - ones[i] for i in range(len(strs))]
        
        @cache
        def maxSubset(i, m, n):
            out = 0
            if m == n == 0 or i == len(strs): return 0
            if zeros[i] <= m and ones[i] <= n:
                out = maxSubset(i+1, m-zeros[i], n-ones[i]) + 1
            return max(out, maxSubset(i+1, m, n))
        
        return maxSubset(0, m, n)