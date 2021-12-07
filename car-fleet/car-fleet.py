class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        out, prev = len(position), 0
        for pos, dps in sorted(zip(position, speed), reverse=True):
            cur = (target - pos) / dps
            if cur <= prev: out -= 1
            else: prev = cur
        return out