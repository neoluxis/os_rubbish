from typing import List


class Solution:
    """
    LeetCode 217. Contains Duplicate
    https://leetcode.com/problems/contains-duplicate/
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False