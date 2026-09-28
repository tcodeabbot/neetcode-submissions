class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        Map = {}

        for i, n in enumerate(numbers):
            diff = target - n
            if diff in Map:
                return [Map[diff] + 1, i + 1]
            Map[n] = i
    
        