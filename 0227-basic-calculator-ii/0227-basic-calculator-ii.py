class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = "+"

        s += "+"

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch in "+-*/":

                if sign == "+":
                    stack.append(num)

                elif sign == "-":
                    stack.append(-num)

                elif sign == "*":
                    stack.append(stack.pop() * num)

                elif sign == "/":
                    stack.append(int(stack.pop() / num))

                sign = ch
                num = 0

        return sum(stack)