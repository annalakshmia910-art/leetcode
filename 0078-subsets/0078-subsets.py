class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, path):
            if i == len(nums):
                res.append(path[:])
                return
            dfs(i + 1, path)          # Don't take
            path.append(nums[i])      # Take
            dfs(i + 1, path)
            path.pop()

        dfs(0, [])
        return res