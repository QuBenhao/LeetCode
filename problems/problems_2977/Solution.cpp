//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    long long minimumCost(string source, string target, vector<string>& original, vector<string>& changed, vector<int>& cost) {
        
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
	string source = json::parse(inputArray.at(0));
	string target = json::parse(inputArray.at(1));
	vector<string> original = json::parse(inputArray.at(2));
	vector<string> changed = json::parse(inputArray.at(3));
	vector<int> cost = json::parse(inputArray.at(4));
	return solution.minimumCost(source, target, original, changed, cost);
}
