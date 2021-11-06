class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        axorb = reduce(lambda a, b: a^b, nums)
        lsb = axorb & -axorb
        buckets = [0, 0]
        for num in nums:
            buckets[num & lsb > 0] ^= num
        return buckets
        
        
        
        
        
        
        
        