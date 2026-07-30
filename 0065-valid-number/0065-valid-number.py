class Solution:
    def isNumber(self, s: str) -> bool:
        num = dot = exp = False
        for i, c in enumerate(s):
            if c.isdigit():
                num = True
            elif c in '+-':
                if i > 0 and s[i-1] not in 'eE':
                    return False
            elif c == '.':
                if dot or exp:
                    return False
                dot = True
            elif c in 'eE':
                if exp or not num:
                    return False
                exp = True
                num = False
            else:
                return False
        return num