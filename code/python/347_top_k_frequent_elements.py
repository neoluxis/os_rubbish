from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        返回出现频率前 k 高的元素。
        时间复杂度：O(n log k)
        空间复杂度：O(n)
        """
        # 1. 统计频率
        freq = Counter(nums)  # O(n)
        
        # 2. 维护一个大小为 k 的小顶堆
        # 堆中元素为 (频率, 数字)
        heap = []
        for num, count in freq.items():  # O(n)
            heapq.heappush(heap, (count, num))  # O(log k)
            if len(heap) > k:
                heapq.heappop(heap)  # 弹出最小频率，O(log k)
        
        # 3. 提取堆中元素并返回
        return [item[1] for item in heap]