//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maximumBeauty(vector<int>& nums, int k) {
        int m = 0;
        for (auto num: nums) {
            m = max(m, num);
        }
        auto diffs = vector<int>(m + 2);
        for (auto num: nums) {
            diffs[max(0, num - k)]++;
            diffs[min(m + 1, num + k + 1)]--;
        }
        int ans = 0, cur = 0;
        for (auto v: diffs) {
            cur += v;
            ans = max(ans, cur);
        }
        return ans;
    }
};

json leetcode::qubh::Solve(string input)
{
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
	int k = json::parse(inputArray.at(1));
	return solution.maximumBeauty(nums, k);
}
