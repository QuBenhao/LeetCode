//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    void merge(vector<int>& A, int m, vector<int>& B, int n) {
        
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
	vector<int> A = json::parse(inputArray.at(0));
	int m = json::parse(inputArray.at(1));
	vector<int> B = json::parse(inputArray.at(2));
	int n = json::parse(inputArray.at(3));
	solution.merge(A, m, B, n);
	return A;
}
