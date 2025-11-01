from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        # 按区间左端点排序
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for interval in intervals:
            # 如果 merged 为空或当前区间与上一区间不重叠
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                # 合并区间
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged