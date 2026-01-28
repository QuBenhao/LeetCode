//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    long long minimumCost(string source, string target, vector<char>& original, vector<char>& changed, vector<int>& cost) {
        
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
	vector<string> original_str = json::parse(inputArray.at(2));
	auto original = vector<char>(original_str.size());
	for (size_t i = 0; i < original.size(); ++i) {
		original[i] = original_str[i][0];
	}
	vector<string> changed_str = json::parse(inputArray.at(3));
	auto changed = vector<char>(changed_str.size());
	for (size_t i = 0; i < changed.size(); ++i) {
		changed[i] = changed_str[i][0];
	}
	vector<int> cost = json::parse(inputArray.at(4));
	return solution.minimumCost(source, target, original, changed, cost);
}
