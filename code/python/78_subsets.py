class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        78. Subsets
        Given an integer array nums of unique elements, return all possible subsets (the power set).
        Time  : O(2^n)
        Space : O(n) without counting output
        """
        res: list[list[int]] = []

        def backtrack(start: int, path: list[int]) -> None:
            res.append(path.copy())          # every path is a valid subset
            for i in range(start, len(nums)):
                path.append(nums[i])         # choose
                backtrack(i + 1, path)       # explore
                path.pop()                   # un-choose

        backtrack(0, [])
        return res