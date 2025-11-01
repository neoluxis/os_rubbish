use std::vec::Vec;

impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut res = vec![1; n];

        // left pass: res[i] = product of all elements to the left of i
        for i in 1..n {
            res[i] = res[i - 1] * nums[i - 1];
        }

        // right pass: multiply by product of all elements to the right of i
        let mut right_prod = 1;
        for i in (0..n).rev() {
            res[i] *= right_prod;
            right_prod *= nums[i];
        }

        res
    }
}