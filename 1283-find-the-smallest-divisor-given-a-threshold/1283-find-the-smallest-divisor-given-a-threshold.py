class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)

        while low <= high:
            divisor = (low + high) // 2

            total = 0

            for num in nums:
                total += (num + divisor - 1) // divisor

            if total <= threshold:
                high = divisor - 1
            else:
                low = divisor + 1

        return low
