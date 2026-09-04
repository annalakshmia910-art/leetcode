class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        distance = [float('inf')] * n
        distance[0] = 0
        total = 0
        for _ in range(n):
            # Find the nearest unvisited point
            cur = -1
            for i in range(n):
                if not visited[i] and (cur == -1 or distance[i] < distance[cur]):
                    cur = i
            # Connect the point
            visited[cur] = True
            total += distance[cur]
            # Update distances
            for i in range(n):
                if not visited[i]:
                    x = abs(points[cur][0] - points[i][0])
                    y = abs(points[cur][1] - points[i][1])
                    cost = x + y
                    if cost < distance[i]:
                        distance[i] = cost
        return total