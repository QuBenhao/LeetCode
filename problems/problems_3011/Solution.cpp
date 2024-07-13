//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
private:
    int BitsCount(int n) {
        int count = 0;
        while (n) {
            count += n & 1;
            n >>= 1;
        }
        return count;
    }
public:
    bool canSortArray(vector<int>& nums) {
        for (int i = 0, pre_max = 0, n = static_cast<int>(nums.size()); i < n;) {
            auto ones = BitsCount(nums[i]), cur_max = 0;
            for (; i < n && BitsCount(nums[i]) == ones; i++) {
                if (nums[i] < pre_max) {
                    return false;
                }
                cur_max = max(cur_max, nums[i]);
            }
            pre_max = cur_max;
        }
        return true;
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
	return solution.canSortArray(nums);
}
