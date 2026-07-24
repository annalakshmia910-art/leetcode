class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        a, b = abs(dividend), abs(divisor)
        ans = 0

        while a >= b:
            temp, count = b, 1
            while a >= (temp << 1):
                temp <<= 1
                count <<= 1
            a -= temp
            ans += count

        ans *= sign
        return min(max(-2**31, ans), 2**31 - 1)
