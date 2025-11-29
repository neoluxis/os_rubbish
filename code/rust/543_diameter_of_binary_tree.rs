use std::rc::Rc;
use std::cell::RefCell;

type TreeNodeRef = Rc<RefCell<TreeNode>>;

impl Solution {
    pub fn diameter_of_binary_tree(root: Option<TreeNodeRef>) -> i32 {
        let mut best = 0;
        Self::dfs(root, &mut best);
        best
    }

    // 返回以当前节点为根的子树的最大深度
    fn dfs(node: Option<TreeNodeRef>, best: &mut i32) -> i32 {
        match node {
            None => -1, // 空节点深度为 -1，使得叶子深度为 0
            Some(n) => {
                let left  = Self::dfs(n.borrow().left.clone(),  best);
                let right = Self::dfs(n.borrow().right.clone(), best);
                // 经过当前节点的最长路径长度
                *best = (*best).max(left + right + 2);
                // 返回子树深度
                left.max(right) + 1
            }
        }
    }
}

// ---------- TreeNode definition provided by LeetCode ----------
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<TreeNodeRef>,
    pub right: Option<TreeNodeRef>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> TreeNodeRef {
        Rc::new(RefCell::new(TreeNode { val, left: None, right: None }))
    }
}

pub struct Solution;