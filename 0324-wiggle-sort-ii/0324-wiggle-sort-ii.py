class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res=[]
        nums.sort()
        n=len(nums)
        l=(n-1)//2
        r=n-1
        for i in range(n):
            if i%2==0:
                res.append(nums[l])
                l-=1
            else:
                res.append(nums[r])
                r-=1
        nums[:]=res