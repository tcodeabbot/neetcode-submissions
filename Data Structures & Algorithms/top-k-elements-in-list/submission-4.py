from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1:1
        2:2
        3:3

        """
        count = Counter(nums)

        heap = []

        for n, c in count.items():
            heapq.heappush(heap, (c, n))
            while len(heap) > k:
                heapq.heappop(heap)
        result = [n for c, n in heap]
        return result
            