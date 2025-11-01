from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        136. Single Number
        https://leetcode.com/problems/single-number/
        """
        xor = 0
        for n in nums:
            xor ^= n
        return xor