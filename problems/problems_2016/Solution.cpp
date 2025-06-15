//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maximumDifference(vector<int>& nums) {
      int ans = -1;
      int minVal = nums[0];
      for (auto num: nums) {
        if (num > minVal) {
          ans = max(ans, num - minVal);
        }
        minVal = min(minVal, num);
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
	return solution.maximumDifference(nums);
}
