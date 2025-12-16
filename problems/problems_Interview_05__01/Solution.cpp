//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int insertBits(int N, int M, int i, int j) {
      for (int idx = i; idx <= j; ++idx) {
				if ((M >> (idx - i)) & 1) {
					N |= 1 << idx;
				} else if ((N >> idx) & 1) {
					N ^= 1 << idx;
				}
			}
			return N;
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
	int N = json::parse(inputArray.at(0));
	int M = json::parse(inputArray.at(1));
	int i = json::parse(inputArray.at(2));
	int j = json::parse(inputArray.at(3));
	return solution.insertBits(N, M, i, j);
}
