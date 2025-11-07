/// 48. Rotate Image
/// https://leetcode.com/problems/rotate-image/
///
/// You are given an n x n 2D matrix representing an image, rotate it by 90 degrees (clockwise).
/// You must rotate the image in-place, i.e., modify the input 2D matrix directly.
/// DO NOT allocate another 2D matrix and do the rotation.
///
/// Constraints:
///   n == matrix.len() == matrix[i].len()
///   1 <= n <= 20
///   -1000 <= matrix[i][j] <= 1000

pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
    let n = matrix.len();

    // 1. Transpose the matrix: swap matrix[i][j] with matrix[j][i]
    for i in 0..n {
        for j in i + 1..n {
            let tmp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = tmp;
        }
    }

    // 2. Reverse each row to complete the 90-degree clockwise rotation
    for row in matrix.iter_mut() {
        row.reverse();
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example1() {
        let mut m = vec![
            vec![1, 2, 3],
            vec![4, 5, 6],
            vec![7, 8, 9],
        ];
        rotate(&mut m);
        assert_eq!(m, vec![
            vec![7, 4, 1],
            vec![8, 5, 2],
            vec![9, 6, 3],
        ]);
    }

    #[test]
    fn example2() {
        let mut m = vec![
            vec![5, 1, 9, 11],
            vec![2, 4, 8, 10],
            vec![13, 3, 6, 7],
            vec![15, 14, 12, 16],
        ];
        rotate(&mut m);
        assert_eq!(m, vec![
            vec![15, 13, 2, 5],
            vec![14, 3, 4, 1],
            vec![12, 6, 8, 9],
            vec![16, 7, 10, 11],
        ]);
    }
}