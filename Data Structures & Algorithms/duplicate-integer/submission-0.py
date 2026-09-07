class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Map = {}

        if not nums:
            return False

        for i,n in enumerate(nums):
            if n in Map:
                return True
            Map[n] = i
        return False
