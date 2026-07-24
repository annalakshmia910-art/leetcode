class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            k = n - 1
            while nums[k] <= nums[i]:
                k -= 1
            nums[i], nums[k] = nums[k], nums[i]

        nums[i + 1:] = nums[i + 1:][::-1]