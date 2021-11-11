object Solution {
    def minStartValue(nums: Array[Int]): Int = {
        var cur = 0;
        var mn = 0;
        for (num <- nums) {
            cur += num;
            if (cur < mn) mn = cur;
        }
        return 1 - mn;
    }
}