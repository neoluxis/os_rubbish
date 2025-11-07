from typing import List

class Solution:
    """
    LeetCode 349. Intersection of Two Arrays
    https://leetcode.com/problems/intersection-of-two-arrays/
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert both lists to sets to remove duplicates and enable O(1) lookups
        set1, set2 = set(nums1), set(nums2)
        # Return the intersection as a list
        return list(set1 & set2)