class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Edge case
        if len(nums) == 1: return nums[0]
        
        prod = lambda arr : reduce(lambda a, b: a*b, arr) if arr else 0
        
        # Create partitions such that each partition is seperated by a zero
        cur, negCnt = [], 0
        numPartitions = []
        for num in nums:
            if num > 0:
                cur += [num]
            elif num < 0:
                cur += [num]
                negCnt += 1
            else:
                numPartitions += [(cur, negCnt)]
                cur, negCnt = [], 0
        numPartitions += [(cur, negCnt)]
        
        # Find the max value of all partitions
        mx = nums[0]
        for partition, negCnt in numPartitions:
            # Negatives do not all cancel left and right sub partitions must be made to compute max 
            if negCnt % 2:
                l, r = 0, len(partition) - 1
                while (a:=partition[l] > 0) or partition[r] > 0:
                    if a: l+=1
                    if partition[r] > 0: r-=1
                mx = max(mx, prod(partition[:r]))
                mx = max(mx, prod(partition[l+1:]))
            # Negatives cancel, max of this partition is the product of all its elements
            else:
                mx = max(mx, prod(partition))
        
        return mx