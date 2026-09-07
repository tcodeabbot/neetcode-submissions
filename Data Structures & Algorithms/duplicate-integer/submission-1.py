from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        for n, c in counter.items():
            if c > 1:
                return True
        return False