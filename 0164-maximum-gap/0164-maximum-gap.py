class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        max_gap=0
        if n<2:
            return 0
        for i in range(1,n):
            max_gap=max(nums[i]-nums[i-1], max_gap)
        return max_gap
            

