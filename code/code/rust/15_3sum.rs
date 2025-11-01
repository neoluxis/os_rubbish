```rust
impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        nums.sort_unstable();
        let n = nums.len();
        let mut res = Vec::new();
        for i in 0..n {
            if i > 0 && nums[i] == nums[i - 1] { continue; }
            let (mut l, mut r) = (i + 1, n - 1);
            while l < r {
                let sum = nums[i] + nums[l] + nums[r];
                match sum.cmp(&0) {
                    std::cmp::Ordering::Equal => {
                        res.push(vec![nums[i], nums[l], nums[r]]);
                        l += 1;
                        r -= 1;
                        while l < r && nums[l] == nums[l - 1] { l += 1; }
                        while l < r && nums[r] == nums[r + 1] { r -= 1; }
                    }
                    std::cmp::Ordering::Less => l += 1,
                    std::cmp::Ordering::Greater => r -= 1,
                }
            }
        }
        res
    }
}
```