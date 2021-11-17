class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2 == p3 == p4: return False
        p1, p2, p3, p4 = sorted([p1,p2,p3,p4])
        
        sideLength = lambda a, b : pow(b[0] - a[0], 2) + pow(b[1] - a[1], 2)
        
        s1 = sideLength(p1, p2)
        s2 = sideLength(p1, p3)
        s3 = sideLength(p4, p2)
        s4 = sideLength(p4, p3)
        h  = sideLength(p2, p3)
        
        return (s1 == s2 == s3 == s4) and h == 2 * s1