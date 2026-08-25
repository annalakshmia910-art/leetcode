class Solution:
    def shortestPalindrome(self, s: str) -> str:
        for i in range(len(s), -1, -1):
            prefix = s[:i]
            if prefix == prefix[::-1]:
                return s[i:][::-1] + s
        return s