class Solution:
    def sideLength(self, a, b):
        return sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
    
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        p1, p2, p3, p4 = sorted([p1,p2,p3,p4])
        
        if p1 == p2 == p3 == p4: return False
        
        s1 = self.sideLength(p1, p2)
        s2 = self.sideLength(p1, p3)
        s3 = self.sideLength(p4, p2)
        s4 = self.sideLength(p4, p3)
        
        if not (s1 == s2 == s3 == s4): return False
        
        h = self.sideLength(p2, p3)
        return abs(h - sqrt(2)*s1) < .0001