```rust
// 33. Search in Rotated Sorted Array
// https://leetcode.com/problems/search-in-rotated-sorted-array/
//
// There is an integer array nums sorted in ascending order (with distinct values).
// Prior to being passed to your function, nums is possibly rotated at an unknown
// pivot index k (1 <= k < nums.len()) such that the resulting array is
// [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
// For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
// Given the array nums after the possible rotation and an integer target,
// return the index of target if it is in nums, or -1 if it is not in nums.
//
// You must write an algorithm with O(log n) runtime complexity.

pub struct Solution;

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let (mut lo, mut hi) = (0, nums.len() as i32 - 1);
        while lo <= hi {
            let mid = lo + ((hi - lo) >> 1);
            if nums[mid as usize] == target {
                return mid;
            }
            // Determine which half is sorted.
            if nums[lo as usize] <= nums[mid as usize] {
                // Left half is sorted.
                if nums[lo as usize] <= target && target < nums[mid as usize] {
                    hi = mid - 1; // Target lies in left half.
                } else {
                    lo = mid + 1; // Target lies in right half.
                }
            } else {
                // Right half is sorted.
                if nums[mid as usize] < target && target <= nums[hi as usize] {
                    lo = mid + 1; // Target lies in right half.
                } else {
                    hi = mid - 1; // Target lies in left half.
                }
            }
        }
        -1
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn ex1() {
        assert_eq!(Solution::search(vec![4, 5, 6, 7, 0, 1, 2], 0), 4);
    }

    #[test]
    fn ex2() {
        assert_eq!(Solution::search(vec![4, 5, 6, 7, 0, 1, 2], 3), -1);
    }

    #[test]
    fn ex3() {
        assert_eq!(Solution::search(vec![1], 0), -1);
    }

    #[test]
    fn ex4() {
        assert_eq!(Solution::search(vec![1, 3], 3), 1);
    }
}
```