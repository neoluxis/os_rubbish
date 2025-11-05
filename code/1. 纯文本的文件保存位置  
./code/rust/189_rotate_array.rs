```rust
// 189. Rotate Array
// https://leetcode.com/problems/rotate-array/
//
// Given an integer array nums, rotate it to the right by k steps.
//
// Example:
// Input: nums = [1,2,3,4,5,6,7], k = 3
// Output: [5,6,7,1,2,3,4]
//
// Constraints:
// 1 <= nums.len() <= 10^5
// -2^31 <= nums[i] <= 2^31 - 1
// 0 <= k <= 10^5
//
// Follow-up: try to do it in-place with O(1) extra space.

impl Solution {
    pub fn rotate(nums: &mut Vec<i32>, k: i32) {
        let n = nums.len();
        if n == 0 {
            return;
        }
        let k = (k as usize) % n;
        if k == 0 {
            return;
        }

        // Three reversals:
        // 1. reverse entire array
        // 2. reverse first k elements
        // 3. reverse remaining n-k elements
        nums.reverse();
        nums[..k].reverse();
        nums[k..].reverse();
    }
}
```