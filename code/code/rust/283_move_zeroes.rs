pub fn move_zeroes(nums: &mut Vec<i32>) {
    let mut last_non_zero = 0;
    for i in 0..nums.len() {
        if nums[i] != 0 {
            nums.swap(last_non_zero, i);
            last_non_zero += 1;
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example1() {
        let mut v = vec![0, 1, 0, 3, 12];
        move_zeroes(&mut v);
        assert_eq!(v, vec![1, 3, 12, 0, 0]);
    }

    #[test]
    fn example2() {
        let mut v = vec![0];
        move_zeroes(&mut v);
        assert_eq!(v, vec![0]);
    }
}