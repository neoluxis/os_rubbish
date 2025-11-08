# LeetCode 206 – Reverse Linked List
# 单链表就地反转（迭代版）
# 时间复杂度: O(n)  空间复杂度: O(1)

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, nxt: Optional["ListNode"] = None):
        self.val = val
        self.next = nxt

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev: Optional[ListNode] = None
        curr = head
        while curr:
            nxt = curr.next      # 保存后继
            curr.next = prev     # 反转指针
            prev = curr          # 前进一步
            curr = nxt
        return prev