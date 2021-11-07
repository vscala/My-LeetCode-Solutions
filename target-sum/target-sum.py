class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def find(cur, i):
            return int(cur == target) if i == len(nums) else find(cur + nums[i], i+1) + find(cur - nums[i], i+1)
        return find(0, 0)