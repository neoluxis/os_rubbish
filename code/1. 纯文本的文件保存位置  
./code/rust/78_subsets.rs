```rust
impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut res = Vec::new();
        let mut cur = Vec::new();
        fn backtrack(start: usize, nums: &[i32], cur: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
            res.push(cur.clone());
            for i in start..nums.len() {
                cur.push(nums[i]);
                backtrack(i + 1, nums, cur, res);
                cur.pop();
            }
        }
        backtrack(0, &nums, &mut cur, &mut res);
        res
    }
}
```