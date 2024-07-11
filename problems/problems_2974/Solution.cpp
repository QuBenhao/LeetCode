//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> numberGame(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        vector<int> res;
        for (int i = 1; i < static_cast<int>(nums.size()); i += 2) {
            res.push_back(nums[i]);
            res.push_back(nums[i - 1]);
        }
        return res;
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
	return solution.numberGame(nums);
}
