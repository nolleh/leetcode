from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = nums[0]
        left = [x for x in nums if x < pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]

        if len(right) >= k:
            return self.findKthLargest(right, k)
        elif len(right) + len(mid) >= k:
            return pivot
        else:
            return self.findKthLargest(left, k - len(right) - len(mid))

    def findKthLargestUsingHeap(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
