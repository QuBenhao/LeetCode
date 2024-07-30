//go:build ignore
#include "cpp/common/Solution.h"
#include <map>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        map<int, int> m;
        for (int i = 0; i < nums.size(); i++) {
            if (m.find(target - nums[i]) != m.end()) {
                return {m[target - nums[i]], i};
            }
            m[nums[i]] = i;
        }
        return {};
    }
};

json leetcode::qubh::Solve(string input) {
    vector<string> inputArray;
    auto pos = input.find('\n');
    while (pos != string::npos) {
        inputArray.push_back(input.substr(0, pos));
        input = input.substr(pos + 1);
        pos = input.find('\n');
    }
    inputArray.push_back(input);

    Solution solution;
    vector<int> nums = json::parse(inputArray.at(0));
    int target = json::parse(inputArray.at(1));
    return solution.twoSum(nums, target);
}
