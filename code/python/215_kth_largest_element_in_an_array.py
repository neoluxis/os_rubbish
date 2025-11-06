import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        使用大小为 k 的最小堆，堆顶即为第 k 大的元素。
        时间复杂度：O(n log k)
        空间复杂度：O(k)
        """
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]