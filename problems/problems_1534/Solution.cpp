//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int countGoodTriplets(vector<int>& arr, int a, int b, int c) {
        
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
	vector<int> arr = json::parse(inputArray.at(0));
	int a = json::parse(inputArray.at(1));
	int b = json::parse(inputArray.at(2));
	int c = json::parse(inputArray.at(3));
	return solution.countGoodTriplets(arr, a, b, c);
}
