class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter, defaultdict
        
        if not s or not t or len(t) > len(s):
            return ""
        
        need = Counter(t)
        missing = len(t)
        left = 0
        start, end = 0, float('inf')
        
        for right, ch in enumerate(s):
            # 当前字符在 need 中，则减少缺失计数
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
            
            # 当 missing 为 0 时，收缩左边界
            while missing == 0:
                if right - left < end - start:
                    start, end = left, right
                # 移动左指针
                left_ch = s[left]
                need[left_ch] += 1
                # 如果移出的字符是 t 中需要的，则增加 missing
                if need[left_ch] > 0:
                    missing += 1
                left += 1
        
        return "" if end == float('inf') else s[start:end+1]