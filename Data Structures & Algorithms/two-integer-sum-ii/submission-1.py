class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, n in enumerate(numbers):
            diff = target - n
            
            if diff in hashMap:
                return [hashMap[diff], i + 1]
            hashMap[n] = i + 1
        