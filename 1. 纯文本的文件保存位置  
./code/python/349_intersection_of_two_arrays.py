2. 纯文本格式的代码  
```python
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 使用集合去重后求交集
        return list(set(nums1) & set(nums2))
```