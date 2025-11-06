class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        max_len = 0
        
        for n in num_set:
            # Only start counting if 'n' is the left-most of a sequence
            if n - 1 not in num_set:
                cur = n
                cur_len = 1
                
                while cur + 1 in num_set:
                    cur += 1
                    cur_len += 1
                
                max_len = max(max_len, cur_len)
        
        return max_len