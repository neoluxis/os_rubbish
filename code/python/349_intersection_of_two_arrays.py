from typing import List


class Solution:
    """
    LeetCode 349. Intersection of Two Arrays
    https://leetcode.com/problems/intersection-of-two-arrays/
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 使用内置集合求交集，时间复杂度 O(n + m)，空间复杂度 O(n + m)
        return list(set(nums1) & set(nums2))