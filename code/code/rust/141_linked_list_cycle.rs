```rust
// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }

use std::collections::HashSet;

impl Solution {
    pub fn has_cycle(head: Option<Box<ListNode>>) -> bool {
        let mut seen = HashSet::new();
        let mut curr = head.as_ref();
        while let Some(node) = curr {
            let ptr = node.as_ref() as *const ListNode;
            if !seen.insert(ptr) {
                return true;
            }
            curr = node.next.as_ref();
        }
        false
    }
}
```