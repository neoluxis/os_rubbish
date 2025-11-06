from typing import List

class Solution:
    """
    LeetCode 152. Maximum Product Subarray
    https://leetcode.com/problems/maximum-product-subarray/

    Find the contiguous subarray (containing at least one number) which has
    the largest product and return that product.
    """

    def maxProduct(self, nums: List[int]) -> int:
        """
        O(n) time, O(1) space.

        Key idea: maintain both the best product ending at current position
        (`cur_max`) and the worst product (`cur_min`), because a negative
        number can flip the situation.
        """
        if not nums:
            return 0

        # At the first element, all three values are equal.
        global_max = cur_max = cur_min = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            # When x is negative, swap cur_max and cur_min.
            if x < 0:
                cur_max, cur_min = cur_min, cur_max

            # Update running max/min ending at position i.
            cur_max = max(x, cur_max * x)
            cur_min = min(x, cur_min * x)

            # Track global best.
            global_max = max(global_max, cur_max)

        return global_max


# Quick sanity checks
if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProduct([2, 3, -2, 4]) == 6
    assert sol.maxProduct([-2, 0, -1]) == 0
    assert sol.maxProduct([-2]) == -2
    assert sol.maxProduct([0, 2]) == 2