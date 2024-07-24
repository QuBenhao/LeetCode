//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minimumOperations(string num) {
        int n = static_cast<int>(num.size());
        bool zero = false, five = false;
        for (int i = n - 1; i >= 0; i--) {
            auto c = num[i];
            if ((zero && (c == '0' || c == '5')) || (five && (c == '2' || c == '7'))) {
                return n - i - 2;
            }
            if (c == '0') {
                zero = true;
            }
            if (c == '5') {
                five = true;
            }
        }
        return n - zero;
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
	string num = json::parse(inputArray.at(0));
	return solution.minimumOperations(num);
}
