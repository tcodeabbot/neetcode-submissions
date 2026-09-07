class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        An empty subset is valid for any input that we are given.
        Sample test input:
        Input: nums = [1,2,3]
        Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

        """

        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return 

            # decide to include the input at position i

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res
            
