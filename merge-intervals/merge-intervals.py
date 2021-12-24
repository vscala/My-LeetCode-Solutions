class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = [[-1, -1]]
        for s, e in sorted(intervals):
            if s >= out[-1][0] and s <= out[-1][1]:
                if e > out[-1][1]: out[-1][1] = e
            else: out.append([s, e])
        return out[1:]