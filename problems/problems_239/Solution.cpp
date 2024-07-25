//go:build ignore
#include "cpp/common/Solution.h"
#include <deque>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> ans;
        deque<int> q;
        int n = static_cast<int>(nums.size());
        for (int i = 0; i < n; i++) {
            while (!q.empty() && nums[q.back()] <= nums[i]) {
                q.pop_back();
            }
            q.emplace_back(i);
            if (i - q.front() >= k) {
                q.pop_front();
            }
            if (i >= k - 1) {
                ans.emplace_back(nums[q.front()]);
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
	int k = json::parse(inputArray.at(1));
	return solution.maxSlidingWindow(nums, k);
}
