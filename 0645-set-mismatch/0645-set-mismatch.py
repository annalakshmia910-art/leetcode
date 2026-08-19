class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        duplicate = 0
        missing = 0

        for i in range(n):
            index = abs(nums[i]) - 1

            if nums[index] < 0:
                duplicate = abs(nums[i])
            else:
                nums[index] = -nums[index]

        for i in range(n):
            if nums[i] > 0:
                missing = i + 1

        return [duplicate, missing]