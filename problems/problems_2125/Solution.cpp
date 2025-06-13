//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int ans = 0;
		int prev = 0;
		for (const auto& row: bank) {
			int count = 0;
			for (auto c: row) {
				if (c == '1') {
					++count;
				}
			}
			ans += count * prev;
			if (count > 0) {
				prev = count;
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
	vector<string> bank = json::parse(inputArray.at(0));
	return solution.numberOfBeams(bank);
}
