//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    double minTime(int n, int k, int m, vector<int>& time, vector<double>& mul) {
      int total_mask = 1 << n;
			int init_mask = total_mask - 1;
			vector<vector<int>> graph(total_mask);
			for (int i = 1; i < total_mask; ++i) {
				vector<int> bits;
				int bit_count = 0;
				for (int j = 0; j < n; ++j) {
					if (i & (1 << j)) {
						bits.push_back(j);
						++bit_count;
					}
				}
				
			}
			return -1.0;
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
	int n = json::parse(inputArray.at(0));
	int k = json::parse(inputArray.at(1));
	int m = json::parse(inputArray.at(2));
	vector<int> time = json::parse(inputArray.at(3));
	vector<double> mul = json::parse(inputArray.at(4));
	return solution.minTime(n, k, m, time, mul);
}
