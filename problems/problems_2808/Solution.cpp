//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_map>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minimumSeconds(vector<int>& nums) {
        auto idx_map = unordered_map<int, vector<int>>();
        for (int i = 0; i < nums.size(); i++) {
            idx_map[nums[i]].push_back(i);
        }
        int n = static_cast<int>(nums.size()), ans = n;
        for (auto& [_, idxes]: idx_map) {
            int cur = idxes.front() + n - idxes.back();
            for (int i = 1; i < idxes.size(); i++) {
                cur = max(cur, idxes[i] - idxes[i - 1]);
            }
            ans = min(ans, cur);
        }
        return ans / 2;
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
	return solution.minimumSeconds(nums);
}
