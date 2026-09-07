class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}

        for n in nums:
            num_count[n] = 1 + num_count.get(n, 0)
        arr = []
        for num, count in num_count.items():
            arr.append([count, num])
        arr.sort()

        count = 0
        result = []
        while count < k and len(arr) > 0:
            result.append(arr.pop()[1])
            count += 1
        return result