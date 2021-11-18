class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        add_ = lambda a, b : a + b
        sub_ = lambda a, b : a - b
        mul_ = lambda a, b : a * b
        div_ = lambda a, b : b and a / b
        operations = [add_, sub_, mul_, div_]
        for a, b, c, d in permutations(cards):
            for combo in combinations_with_replacement(operations, 3):
                for x, y, z in permutations(combo):
                    if abs(z(y(x(a, b), c), d) - 24) < .0001: return True
                    if abs(z(x(a,b), y(c,d)) - 24) < .0001: return True
                    if abs(z(d, y(x(a, b), c)) - 24) < .0001: return True
                    if abs(z(d, y(c, x(a, b))) - 24) < .0001: return True
        return False