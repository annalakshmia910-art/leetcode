class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = [0] * 1001

        # Count elements of arr1
        for num in arr1:
            count[num] += 1

        result = []

        # Put arr2 elements first
        for num in arr2:
            while count[num] > 0:
                result.append(num)
                count[num] -= 1

        # Put remaining elements in ascending order
        for num in range(1001):
            while count[num] > 0:
                result.append(num)
                count[num] -= 1

        return result