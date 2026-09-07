class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)

        if m * k > n:
            return -1

        left = min(bloomDay)
        right = max(bloomDay)

        while left < right:
            day = (left + right) // 2

            bouquets = 0
            flowers = 0

            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1

                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

            if bouquets >= m:
                right = day
            else:
                left = day + 1

        return left