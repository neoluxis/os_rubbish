from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        349. Intersection of Two Arrays
        https://leetcode.com/problems/intersection-of-two-arrays/
        """
        return list(set(nums1) & set(nums2))