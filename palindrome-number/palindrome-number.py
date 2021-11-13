class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        stack = []
        while x:
            stack += [x%10]
            x //= 10
        return stack == stack[::-1]