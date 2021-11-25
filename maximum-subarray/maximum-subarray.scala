object Solution {
    def maxSubArray(nums: Array[Int]): Int = {
        var cur = 0;
        var out = nums(0);
        for (num <- nums) {
            if (cur > 0) cur += num;
            else cur = num;
            if (cur > out) out = cur;
        }
        out;
    }
}