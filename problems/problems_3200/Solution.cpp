//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
    int f(int n, int m) {
        int odd = sqrt(n);
        int even = (sqrt(m * 4 + 1) - 1) / 2;
        return odd > even ? even * 2 + 1 : odd * 2;
    }

public:
    int maxHeightOfTriangle(int red, int blue) {
        return max(f(red, blue), f(blue, red));
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
	int red = json::parse(inputArray.at(0));
	int blue = json::parse(inputArray.at(1));
	return solution.maxHeightOfTriangle(red, blue);
}
