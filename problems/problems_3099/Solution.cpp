//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int sumOfTheDigitsOfHarshadNumber(int x) {
        auto s = 0;
        for (auto num = x; num > 0; num /= 10) {
            s += num % 10;
        }
        return s != 0 && x % s == 0 ? s : -1;
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
	int x = json::parse(inputArray.at(0));
	return solution.sumOfTheDigitsOfHarshadNumber(x);
}
