class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        A, B, C = [int(c) for c in num1], [int(c) for c in num2], [None] * (len(num1) + len(num2)-1)
        
        for ai, a in enumerate(A):
            for bi, b in enumerate(B):
                if C[ai+bi] == None: C[ai+bi] = a*b
                else: C[ai+bi] += a*b
        
        carry = 0
        for i in range(-1, ~len(C), -1):
            carry, C[i] = divmod(C[i] + carry, 10)
        
        return str(carry) + "".join(map(str, C)) if carry else "".join(map(str, C))