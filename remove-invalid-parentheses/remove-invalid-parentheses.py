class Solution:
    @cache
    def isValid(self, s: str) -> bool:
        open = 0
        for c in s:
            if c == '(': open += 1
            if c == ')':
                if open: open -= 1
                else: return False
        return not open
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        s = [c for c in s]
        
        global out
        out = [""]
        seen = set()
        def backtrack(i):
            global out
            if i == len(s):
                t = "".join(s)
                if t in seen: return
                seen.add(t)
                if self.isValid(t):
                    if len(t) > len(out[-1]): out = [t]
                    elif len(t) == len(out[-1]): out += [t]
                return
            if s[i] not in "()":
                return backtrack(i+1)
            temp = s[i]
            s[i] = ""
            backtrack(i+1) # don't remove s[i]
            s[i] = temp
            backtrack(i+1) # remove s[i]
        backtrack(0)
        if out[0] == "": return [""]
        return out