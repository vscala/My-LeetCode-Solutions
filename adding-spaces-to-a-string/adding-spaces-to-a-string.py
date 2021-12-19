class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        a, b = 0, 0
        out = []
        for i in range(len(s) + len(spaces)):
            if b < len(spaces) and spaces[b] == a: 
                out += [" "]
                b += 1
            else:
                out += [s[a]]
                a += 1
        return "".join(out)