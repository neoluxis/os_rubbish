```python
"""
1. Two Sum
https://leetcode.com/problems/two-sum/
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        使用哈希表一次遍历即可找到答案。
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []  # 题目保证有解，不会走到这里
```