class Solution:
    def calculate(self, s: str) -> int:
        
        # Computer all inner expressions and add to stack
        stack = []  # calculator stack
        openp = []  # left parenthesis indexes
        cur = 0     # cur number
        for c in s:
            if c == ' ': continue           # ignore space
            elif c in '+-':                 # append currente number then operation
                stack += [cur]
                stack += [c]
                cur = 0
            elif c == '(':                  # mark index of open parenthesis
                openp += [len(stack)]
            elif c == ')':                  # computer value between cur and matching parenthesis
                stack += [cur]
                start = openp.pop()
                cur = stack.pop(start)
                while len(stack) != start:
                    op = stack.pop(start)
                    num = stack.pop(start)
                    if op == '+': cur += num
                    else: cur -= num
            else:                           # update current number with c
                cur *= 10
                cur += int(c)
        stack += [cur]                      # append final cur
        
        # Compute remaining operations
        cur = stack.pop(0)                  
        while len(stack):
            op = stack.pop(0)
            num = stack.pop(0)
            if op == '+': cur += num
            else: cur -= num
        return cur
            