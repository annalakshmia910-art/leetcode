class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        n = len(arr)

        for size in range(n, 1, -1):
        # Find the largest element in arr[0:size]
            max_index = 0
            for i in range(1, size):
                if arr[i] > arr[max_index]:
                    max_index = i

        # Already in the correct position
            if max_index == size - 1:
                continue

        # Bring largest element to the front
            if max_index != 0:
                arr[0:max_index + 1] = arr[0:max_index + 1][::-1]
                ans.append(max_index + 1)

        # Move largest element to its final position
            arr[0:size] = arr[0:size][::-1]
            ans.append(size)

        return ans