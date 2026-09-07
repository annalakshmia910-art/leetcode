class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        answer = 0

        while n > 1:
            length = 2 ** (n - 1)
            half = length // 2

            if k > half:
                answer = 1 - answer
                k = k - half

            n -= 1

        return answer