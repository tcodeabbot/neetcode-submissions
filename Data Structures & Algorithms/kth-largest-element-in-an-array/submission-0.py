import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        max_heap = []

        for i in range(len(nums)):
            max_heap.append(-nums[i])

        heapq.heapify(max_heap)
        
        while k > 1:
            heapq.heappop(max_heap)
            k -= 1
        return -heapq.heappop(max_heap)
        
            
