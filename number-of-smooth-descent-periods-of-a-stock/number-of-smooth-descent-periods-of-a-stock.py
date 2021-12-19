class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        out = 0
        prev, val = prices[-1]+2, 0
        for i in range(len(prices) - 1, -1, -1):
            if prices[i] - 1 == prev: 
                val += 1
            else: val = 1
            out += val
            prev = prices[i]
        return out