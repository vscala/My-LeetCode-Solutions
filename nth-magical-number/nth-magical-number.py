class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        g, m = gcd(a, b), (10**9 + 7)
        if g == a: return (a * n) % m
        if g == b: return (b * n) % m
        
        c1, c2, l = a, b, a * b // g
        known = [0]
        while c1 < l or c2 < l:
            if c1 < c2:
                known += [c1]
                c1 += a
            else:
                known += [c2]
                c2 += b
        d, r = divmod(n, len(known))
        return (l * d + known[r]) % m