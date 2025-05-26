//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0, right = numbers.size() - 1;
        while (left < right) {
            int cur = numbers[left] + numbers[right];
            if (cur == target) {
                break;
            } else if (cur < target) {
                left++;
            } else {
                right--;
            }
        }
        return {left, right};
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
	vector<int> numbers = json::parse(inputArray.at(0));
	int target = json::parse(inputArray.at(1));
	return solution.twoSum(numbers, target);
}
