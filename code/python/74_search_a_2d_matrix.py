from typing import List


class Solution:
    """
    LeetCode 74. Search a 2D Matrix
    https://leetcode.com/problems/search-a-2d-matrix/
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            mid_val = matrix[mid // cols][mid % cols]

            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


if __name__ == "__main__":
    sol = Solution()
    mat = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(sol.searchMatrix(mat, 3))  # True
    print(sol.searchMatrix(mat, 13)) # False