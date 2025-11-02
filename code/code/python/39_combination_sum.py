from typing import List


class Solution:
    """
    39. Combination Sum
    https://leetcode.com/problems/combination-sum/description/

    Given an array of distinct integers `candidates` and a target integer `target`,
    return a list of all unique combinations of candidates where the chosen numbers
    sum to target.  The same number may be used unlimited times.

    Example:
        Input: candidates = [2,3,6,7], target = 7
        Output: [[2,2,3],[7]]
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res: List[List[int]] = []

        def backtrack(remain: int, path: List[int], start: int) -> None:
            if remain == 0:
                res.append(path.copy())
                return
            if remain < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(remain - candidates[i], path, i)  # allow reuse
                path.pop()  # undo

        candidates.sort()  # not strictly necessary, but helps pruning
        backtrack(target, [], 0)
        return res


# quick sanity check
if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([2, 3, 6, 7], 7))  # [[2,2,3],[7]]