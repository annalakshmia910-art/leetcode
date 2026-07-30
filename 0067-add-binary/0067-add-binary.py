class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, c, res = len(a)-1, len(b)-1, 0, []
        while i >= 0 or j >= 0 or c:
            s = c
            if i >= 0: s += int(a[i]); i -= 1
            if j >= 0: s += int(b[j]); j -= 1
            res.append(str(s % 2))
            c = s // 2
        return ''.join(res[::-1])