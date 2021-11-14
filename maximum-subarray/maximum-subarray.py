class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur, out = nums[0], nums[0]
        for i in range(1, len(nums)):
            if cur > 0: cur = nums[i] + cur
            else: cur = nums[i]
            if cur > out: out = cur
        return out