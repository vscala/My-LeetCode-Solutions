class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        
        while l <= r:
            m = (l + r) // 2
            
            # num is duplicate and nums[m] is the first occurrence
            if m < len(nums) - 1 and nums[m] == nums[m+1]:
                if (m-l) % 2: r = m - 1
                else: l = m + 2
            
            # num is duplicate and nums[m] is the second occurrence
            elif m > 0 and nums[m] == nums[m-1]:
                if (m-l-1) % 2: r = m - 1
                else: l = m + 1
            
            # num is not duplicate
            else: return nums[m]