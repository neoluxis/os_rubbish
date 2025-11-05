from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        使用双端队列维护当前窗口中可能成为最大值的候选下标。
        队首始终保存当前窗口的最大值下标，队列中的下标对应值单调递减。
        时间复杂度 O(n)，空间复杂度 O(k)。
        """
        q = deque()
        res = []
        for i, val in enumerate(nums):
            # 移除队列中超出窗口左侧边界的下标
            while q and q[0] <= i - k:
                q.popleft()
            # 移除队列中所有比当前值小的下标（它们不可能再成为最大值）
            while q and nums[q[-1]] < val:
                q.pop()
            q.append(i)
            # 当窗口形成后，记录队首对应的最大值
            if i >= k - 1:
                res.append(nums[q[0]])
        return res