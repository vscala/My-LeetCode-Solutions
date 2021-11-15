object Solution {
    def maxPower(s: String): Int = {
        var out = 1;
        var cur = 1;
        
        for (i <- 1 to s.length()-1) {
            if (s.charAt(i) == s.charAt(i-1)) {
                cur += 1;
                if (cur > out) out = cur;
            } else {
                cur = 1;
            }
        }
        
        return out;
    }
}