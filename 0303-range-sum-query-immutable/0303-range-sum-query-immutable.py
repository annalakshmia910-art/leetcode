class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]

        for n in nums:
            self.prefix.append(self.prefix[-1] + n)

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]

        