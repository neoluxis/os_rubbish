from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        704. Binary Search
        https://leetcode.com/problems/binary-search/description/

        Classic iterative binary search on a sorted array.
        Time  : O(log n)
        Space : O(1)
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.search([-1, 0, 3, 5, 9, 12], 9))  # 4
    print(sol.search([-1, 0, 3, 5, 9, 12], 2))  # -1