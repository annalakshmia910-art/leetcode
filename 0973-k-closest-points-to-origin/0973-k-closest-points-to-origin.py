class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return point[0] * point[0] + point[1] * point[1]

        def quickselect(left, right):
            pivot = distance(points[right])
            p = left

            for i in range(left, right):
                if distance(points[i]) <= pivot:
                    points[i], points[p] = points[p], points[i]
                    p += 1

            points[p], points[right] = points[right], points[p]

            if p == k - 1:
                return
            elif p < k - 1:
                quickselect(p + 1, right)
            else:
                quickselect(left, p - 1)

        quickselect(0, len(points) - 1)

        return points[:k]