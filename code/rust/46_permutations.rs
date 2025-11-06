pub struct Solution;

impl Solution {
    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut res = Vec::new();
        let mut used = vec![false; nums.len()];
        let mut path = Vec::with_capacity(nums.len());
        Self::backtrack(&nums, &mut used, &mut path, &mut res);
        res
    }

    fn backtrack(nums: &[i32], used: &mut [bool], path: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
        if path.len() == nums.len() {
            res.push(path.clone());
            return;
        }
        for i in 0..nums.len() {
            if used[i] { continue; }
            used[i] = true;
            path.push(nums[i]);
            Self::backtrack(nums, used, path, res);
            path.pop();
            used[i] = false;
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example1() {
        let mut ans = Solution::permute(vec![1, 2, 3]);
        ans.sort();
        let expected: Vec<Vec<i32>> = vec![
            vec![1, 2, 3],
            vec![1, 3, 2],
            vec![2, 1, 3],
            vec![2, 3, 1],
            vec![3, 1, 2],
            vec![3, 2, 1],
        ];
        assert_eq!(ans, expected);
    }

    #[test]
    fn example2() {
        assert_eq!(Solution::permute(vec![0, 1]), vec![vec![0, 1], vec![1, 0]]);
    }

    #[test]
    fn example3() {
        assert_eq!(Solution::permute(vec![1]), vec![vec![1]]);
    }
}