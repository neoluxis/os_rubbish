// LeetCode 206. Reverse Linked List
// https://leetcode.com/problems/reverse-linked-list/
//
// Iterative solution with O(n) time and O(1) extra space.

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

pub struct Solution;

impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut prev = None;
        let mut curr = head;

        while let Some(mut node) = curr {
            let next = node.next.take();
            node.next = prev;
            prev = Some(node);
            curr = next;
        }
        prev
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn build_list(values: &[i32]) -> Option<Box<ListNode>> {
        let mut head = None;
        for &v in values.iter().rev() {
            let mut node = ListNode::new(v);
            node.next = head;
            head = Some(Box::new(node));
        }
        head
    }

    fn collect_list(head: Option<Box<ListNode>>) -> Vec<i32> {
        let mut vals = Vec::new();
        let mut cur = head.as_ref();
        while let Some(node) = cur {
            vals.push(node.val);
            cur = node.next.as_ref();
        }
        vals
    }

    #[test]
    fn test_reverse() {
        let head = build_list(&[1, 2, 3, 4, 5]);
        let reversed = Solution::reverse_list(head);
        assert_eq!(collect_list(reversed), vec![5, 4, 3, 2, 1]);
    }
}