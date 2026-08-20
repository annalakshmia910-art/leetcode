class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights.copy()

    # Simple bubble sort
        n = len(expected)
        for i in range(n):
            for j in range(n - i - 1):
                if expected[j] > expected[j + 1]:
                    expected[j], expected[j + 1] = expected[j + 1], expected[j]

        count = 0

        for i in range(n):
            if heights[i] != expected[i]:
                count += 1

        return count