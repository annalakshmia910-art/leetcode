class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        for h in range(n, 0, -1):
            count = 0

            for citation in citations:
                if citation >= h:
                    count += 1

            if count >= h:
                return h

        return 0