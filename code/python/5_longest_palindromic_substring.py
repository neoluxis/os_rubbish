class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        start, max_len = 0, 1
        
        def expand(l: int, r: int) -> None:
            nonlocal start, max_len
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > max_len:
                    start, max_len = l, r - l + 1
                l -= 1
                r += 1
        
        for i in range(n):
            expand(i, i)      # odd length
            expand(i, i + 1)  # even length
        
        return s[start:start + max_len]