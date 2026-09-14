from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for n, f in count.items():
            heapq.heappush(heap, (f, n))
            while len(heap) > k:
                heapq.heappop(heap)
        return [f for c, f in heap]