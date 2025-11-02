#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> subsets(std::vector<int>& nums) {
        std::vector<std::vector<int>> result;
        std::vector<int> current;
        backtrack(nums, 0, current, result);
        return result;
    }

private:
    void backtrack(const std::vector<int>& nums,
                   int start,
                   std::vector<int>& current,
                   std::vector<std::vector<int>>& result) {
        result.push_back(current);
        for (int i = start; i < nums.size(); ++i) {
            current.push_back(nums[i]);
            backtrack(nums, i + 1, current, result);
            current.pop_back();
        }
    }
};