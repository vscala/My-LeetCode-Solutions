object Solution {
    def hammingDistance(x: Int, y: Int): Int = {
        var z = y ^ x;
        var out = 0;
        while (z > 0) {
            out += 1;
            z = z & z-1;
        }
        return out;
    }
}