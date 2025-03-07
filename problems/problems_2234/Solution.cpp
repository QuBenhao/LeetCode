//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    long long maximumBeauty(vector<int>& flowers, long long newFlowers, int target, int full, int partial) {
        
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
	vector<int> flowers = json::parse(inputArray.at(0));
	long long newFlowers = json::parse(inputArray.at(1));
	int target = json::parse(inputArray.at(2));
	int full = json::parse(inputArray.at(3));
	int partial = json::parse(inputArray.at(4));
	return solution.maximumBeauty(flowers, newFlowers, target, full, partial);
}
