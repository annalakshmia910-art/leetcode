
import heapq

class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        g = [[] for _ in range(n)]

        for (u, v), p in zip(edges, succProb):
            g[u].append((v, p))
            g[v].append((u, p))

        prob = [0.0] * n
        prob[start] = 1.0
        pq = [(-1.0, start)]

        while pq:
            p, u = heapq.heappop(pq)
            p = -p

            if u == end:
                return p

            if p < prob[u]:
                continue

            for v, w in g[u]:
                if p * w > prob[v]:
                    prob[v] = p * w
                    heapq.heappush(pq, (-prob[v], v))

        return 0.0
