use std::collections::HashSet;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut seen = HashSet::with_capacity(nums.len());
        for &n in &nums {
            if !seen.insert(n) {
                return true;
            }
        }
        false
    }
}