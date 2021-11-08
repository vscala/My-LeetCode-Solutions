class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        f1 = f2 = False
        out = []
        for word in text.split():
            if f2:
                out += [word]
                f2 = False
            if f1:
                if word == second: f2 = True
                f1 = False
            if word == first:
                f1 = True
        return out