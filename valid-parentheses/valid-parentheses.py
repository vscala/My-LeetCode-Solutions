class Solution:
    def isValid(self, s: str) -> bool:
        s, i, m = list(s), 0, {")" : "(", "]" : "[", "}" : "{"}
        while i < len(s):
            if s[i] in m:
                if i == 0: return False
                if s[i-1] != m[s[i]]: return False
                del s[i-1]; del s[i-1];
                i -= 1
            else: i += 1
        return not s