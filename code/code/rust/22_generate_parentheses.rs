use std::collections::VecDeque;

impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let mut res = Vec::new();
        let mut queue: VecDeque<(String, i32, i32)> = VecDeque::new();
        // (current string, open count, close count)
        queue.push_back(("".to_string(), 0, 0));

        while let Some((s, open, close)) = queue.pop_front() {
            if open == n && close == n {
                res.push(s);
                continue;
            }
            if open < n {
                queue.push_back((format!("{}(", s), open + 1, close));
            }
            if close < open {
                queue.push_back((format!("{})", s), open, close + 1));
            }
        }
        res
    }
}