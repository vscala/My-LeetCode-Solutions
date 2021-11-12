class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        right = []
        out = []
        nums.reverse()
        for num in nums:
            i = bisect_left(right, num)
            out += [i]
            right.insert(i, num)
        return out[::-1]