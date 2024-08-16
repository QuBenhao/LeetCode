//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int splitNum(int num) {
        vector<int> nums;
        while (num > 0) {
            int r = num % 10;
            if (r != 0) {
                nums.emplace_back(r);
            }
            num /= 10;
        }
        sort(nums.begin(), nums.end());
        int a = 0, b = 0;
        for (int i = 0; i < static_cast<int>(nums.size()); i++) {
            if ((i & 1) == 1) {
                b = b * 10 + nums[i];
            } else {
                a = a * 10 + nums[i];
            }
        }
        return a + b;
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
	int num = json::parse(inputArray.at(0));
	return solution.splitNum(num);
}
