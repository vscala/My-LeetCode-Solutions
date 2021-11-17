class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = [""]
        for word in words:
            word = word.strip()
            if not lines[-1]:
                lines += [word]
            elif len(lines[-1]) + len(word) < maxWidth:
                lines[-1] += " " + word
            else:
                lines += [word]
        
        if not lines[0]: del lines[0]
        if len(lines) > 1:
            for i, line in enumerate(lines[:-1]):
                line = line.split()
                n = sum(len(word) for word in line)
                if len(line) == 1: lines[i] = line[0] + " " * (maxWidth - n)
                else:
                    spaces, extra = divmod(maxWidth - n, len(line)-1)
                    cur = ""
                    for word in line[:-1]:
                        cur += word
                        cur += " " * spaces
                        cur += " " * (extra > 0)
                        extra -= 1
                    cur += line[-1]
                    lines[i] = cur
        if lines[-1][0] == " ": lines[-1] = lines[-1][1:]
        extra = maxWidth - sum(len(word) for word in lines[-1])
        lines[-1] += " " * extra
        return lines