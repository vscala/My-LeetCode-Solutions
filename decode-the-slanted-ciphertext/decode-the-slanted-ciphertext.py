class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText) // rows
        out = []
        for i in range(n):
            for r in range(rows):
                if n * r + r + i < len(encodedText): 
                    out += [encodedText[n * r + r + i]]
        while out and out[-1] == " ": del out[-1]
        return "".join(out)