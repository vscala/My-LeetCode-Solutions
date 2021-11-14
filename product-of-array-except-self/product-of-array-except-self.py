class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = nums.count(0)
        if zeros == 0:
            prod = reduce(lambda a, b : a*b, nums)
            return [prod//num for num in nums]
        elif zeros == 1:
            zeroind = nums.index(0)
            proda = reduce(lambda a, b : a*b, nums[:zeroind]) if nums[:zeroind] else 1
            prodb = reduce(lambda a, b : a*b, nums[zeroind+1:]) if nums[zeroind+1:] else 1
            out = [0 for i in range(len(nums))]
            out[zeroind] = proda * prodb
            return out
        else:
            return [0 for i in range(len(nums))]