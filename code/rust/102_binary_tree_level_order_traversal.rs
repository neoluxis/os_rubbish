use std::rc::Rc;
use std::cell::RefCell;

type TreeLink = Option<Rc<RefCell<TreeNode>>>;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: TreeLink,
    pub right: TreeLink,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

pub fn level_order(root: TreeLink) -> Vec<Vec<i32>> {
    let mut ans = Vec::new();
    if root.is_none() {
        return ans;
    }

    use std::collections::VecDeque;
    let mut q = VecDeque::new();
    q.push_back(root);

    while !q.is_empty() {
        let level_size = q.len();
        let mut level = Vec::with_capacity(level_size);

        for _ in 0..level_size {
            if let Some(node_link) = q.pop_front() {
                if let Some(node) = node_link {
                    let node_ref = node.borrow();
                    level.push(node_ref.val);

                    if node_ref.left.is_some() {
                        q.push_back(node_ref.left.clone());
                    }
                    if node_ref.right.is_some() {
                        q.push_back(node_ref.right.clone());
                    }
                }
            }
        }
        ans.push(level);
    }
    ans
}