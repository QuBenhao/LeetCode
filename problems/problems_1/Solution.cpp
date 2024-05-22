#include <vector>
#include "StringUtil.h"
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {};
    }

    json Solve(string input) {
        vector<string> parts = Split(input, "\n");
        int idx = input.find("\n");
        vector<int> nums = json::parse(input.substr(0, idx));
        int target = json::parse(input.substr(idx + 1));
        return json::parse(twoSum(nums, target));
    }
};
