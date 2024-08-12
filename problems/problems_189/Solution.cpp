//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
		auto reverse = [&](int l, int r) {
			while (l < r) {
				swap(nums[l++], nums[r--]);
			}
		};
		int n = static_cast<int>(nums.size());
		k %= n;
		reverse(0, n - 1);
		reverse(0, k - 1);
		reverse(k, n - 1);
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
	int k = json::parse(inputArray.at(1));
	solution.rotate(nums, k);
	return nums;
}
