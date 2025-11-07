pub fn length_of_lis(nums: Vec<i32>) -> i32 {
    let mut tails = Vec::new();
    for &x in &nums {
        match tails.binary_search(&x) {
            Ok(_) => {} // duplicate, skip
            Err(i) => {
                if i == tails.len() {
                    tails.push(x);
                } else {
                    tails[i] = x;
                }
            }
        }
    }
    tails.len() as i32
}