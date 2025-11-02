impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let (mut l, mut r) = (0, nums.len() as i32 - 1);
        while l <= r {
            let m = l + (r - l) / 2;
            match nums[m as usize].cmp(&target) {
                std::cmp::Ordering::Equal => return m,
                std::cmp::Ordering::Less => l = m + 1,
                std::cmp::Ordering::Greater => r = m - 1,
            }
        }
        -1
    }
}