//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maxDifference(string s) {
        array<int, 26> counts;
        for (auto c: s) {
            counts[c - 'a']++;
        }
        int maxOdd = 0, minEven = s.length();
        for (auto v: counts) {
            if (v == 0) {
                continue;
            }
            if (v % 2 == 1) {
                maxOdd = max(maxOdd, v);
            } else {
                minEven = min(minEven, v);
            }
        }
        return maxOdd - minEven;
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
	string s = json::parse(inputArray.at(0));
	return solution.maxDifference(s);
}
