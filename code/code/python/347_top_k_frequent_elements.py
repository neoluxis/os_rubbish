from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 统计频率
        freq = Counter(nums)
        # 使用最小堆维护出现频率最高的 k 个元素
        # 堆中保存的是 (频率, 数字) 对
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            # 当堆的大小超过 k 时，弹出频率最小的元素
            if len(heap) > k:
                heapq.heappop(heap)
        # 堆中剩下的即为前 k 个高频元素
        return [item[1] for item in heap]