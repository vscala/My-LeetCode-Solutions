class Solution:
    def decodeString(self, s: str) -> str:
        if not "[" in s: return s
        subs = []
        n, a = "", ""
        inpar = 0
        for c in s:
            if c == "[":
                if inpar: a += "["
                inpar += 1
            elif c == "]":
                inpar -= 1
                if inpar: a += "]"
                if not inpar:
                    subs += [(int(n) if n else 1, a)]
                    n, a = "", ""
            elif inpar or c.isalpha():
                a += c
            else:
                if a: 
                    subs += [(1, a)]
                    n, a = "", ""
                n += c
        if a: subs += [(1, a)]
        return "".join(a * self.decodeString(b) for a, b in subs)