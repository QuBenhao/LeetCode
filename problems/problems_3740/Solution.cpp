//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minimumDistance(vector<int>& nums) {
        int ans = INT_MAX;
        unordered_map<int, vector<int>> record;
        for (int k = 0; k < nums.size(); k++) {
            record[nums[k]].push_back(k);
            if (record[nums[k]].size() > 2) {
                int i = record[nums[k]][record[nums[k]].size() - 3];
                ans = min(ans, (k - i) * 2);
            }
        }
        return ans == INT_MAX ? -1 : ans;
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
	return solution.minimumDistance(nums);
}
