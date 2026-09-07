class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(x) for x in nums]

        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        nums.sort(key=cmp_to_key(compare))

        if nums[0] == "0":
            return "0"

        result = ""
        for num in nums:
            result += num

        return result