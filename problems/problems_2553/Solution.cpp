//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> separateDigits(vector<int> &nums) {
        vector<int> ans;
        for (auto num: nums) {
            vector<int> cur;
            while (num > 0) {
                cur.emplace_back(num % 10);
                num /= 10;
            }
            for (int i = static_cast<int>(cur.size()) - 1; i >= 0; --i) {
                ans.emplace_back(cur[i]);
            }
        }
        return ans;
    }
};

json leetcode::qubh::Solve(string input_json_values) {
    vector<string> inputArray;
    size_t pos = input_json_values.find('\n');
    while (pos != string::npos) {
        inputArray.push_back(input_json_values.substr(0, pos));
        input_json_values = input_json_values.substr(pos + 1);
        pos = input_json_values.find('\n');
    }
    inputArray.push_back(input_json_values);

    Solution solution;
    vector<int> nums = json::parse(inputArray.at(0));
    return solution.separateDigits(nums);
}
