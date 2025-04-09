//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    long long numberOfPowerfulInt(long long start, long long finish, int limit, string s) {
        
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
	long long start = json::parse(inputArray.at(0));
	long long finish = json::parse(inputArray.at(1));
	int limit = json::parse(inputArray.at(2));
	string s = json::parse(inputArray.at(3));
	return solution.numberOfPowerfulInt(start, finish, limit, s);
}
