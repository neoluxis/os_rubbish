class Solution:
    def climbStairs(self, n: int) -> int:
        # 本质上是斐波那契数列
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b