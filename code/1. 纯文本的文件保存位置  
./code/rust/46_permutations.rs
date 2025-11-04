2. 纯文本格式的代码  
```rust
// 46. Permutations
// https://leetcode.com/problems/permutations/
impl Solution {
    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
        fn backtrack(
            nums: &Vec<i32>,
            used: &mut Vec<bool>,
            current: &mut Vec<i32>,
            result: &mut Vec<Vec<i32>>,
        ) {
            if current.len() == nums.len() {
                result.push(current.clone());
                return;
            }
            for i in 0..nums.len() {
                if used[i] {
                    continue;
                }
                used[i] = true;
                current.push(nums[i]);
                backtrack(nums, used, current, result);
                current.pop();
                used[i] = false;
            }
        }

        let mut result = Vec::new();
        let mut used = vec![false; nums.len()];
        let mut current = Vec::new();
        backtrack(&nums, &mut used, &mut current, &mut result);
        result
    }
}
```