class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        self.nums=nums
    def sumRange(self, left, right):
        sum=0
        for i in range(left, right+1):
            if i<=right:
                sum+=self.nums[i]
        return sum

        