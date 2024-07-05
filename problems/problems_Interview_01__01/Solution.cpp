//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    bool isUnique(string astr) {
        int mark = 0;
        for (auto c: astr) {
            if (auto cur = 1 << (c - 'a'); (mark & cur) != 0) {
                return false;
            } else {
                mark |= cur;
            }
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
	string astr = json::parse(inputArray.at(0));
	return solution.isUnique(astr);
}
