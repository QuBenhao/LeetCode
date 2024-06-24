//go:build ignore
#include "cpp/common/Solution.h"
#include <stack>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        size_t n = nums.size();
        auto ans = vector<int>(n, -1);
        auto st = stack<size_t>();
        for (size_t i = 0; i < n * 2; i++) {
            while (!st.empty() && nums[st.top()] < nums[i % n]) {
                ans[st.top()] = nums[i % n];
                st.pop();
            }
            if (i < n) {
                st.push(i);
            } else if (st.empty()){
                break;
            }
        }
        return ans;
    }
};

json leetcode::qubh::Solve(string input) {
	vector<string> inputArray;
	size_t pos = input.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find('\n');
	}
	inputArray.push_back(input);

	Solution solution;
	vector<int> nums = json::parse(inputArray.at(0));
	return solution.nextGreaterElements(nums);
}
