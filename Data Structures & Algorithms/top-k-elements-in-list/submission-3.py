from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        min_heap = []

        for n, c in count.items():
            heapq.heappush(min_heap, (c, n))
            while len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [n for c, n in min_heap]

        
