//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int arraySign(vector<int>& nums) {
        int cnt = 0;
        for (auto num: nums) {
            if (num == 0) {
                return 0;
            } else if (num < 0) {
                cnt++;
            }
        }
        return (cnt & 1) == 1 ? -1 : 1;
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
	return solution.arraySign(nums);
}
