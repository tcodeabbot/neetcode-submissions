import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = {}

        for n in nums:
            nums_count[n] = 1 + nums_count.get(n, 0)
        print(nums_count)
        arr = []
        
        for num, count in nums_count.items():
            arr.append([-count, num])
        heapq.heapify(arr)
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(arr)[1])
        return result