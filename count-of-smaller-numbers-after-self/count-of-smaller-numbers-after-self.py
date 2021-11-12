class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        right, out = [], []
        for j in range(-1, ~len(nums), -1):
            i = bisect_left(right, nums[j])
            out += [i]
            right.insert(i, nums[j])
        return out[::-1]