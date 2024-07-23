//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_set>


using namespace std;
using json = nlohmann::json;

class Solution {
private:
    unordered_set<int> square_nums;
    bool is_reachable(int n, int count) {
        if (count == 1) {
            return square_nums.find(n) != square_nums.end();
        }
        for (auto square: square_nums) {
            if (is_reachable(n - square, count - 1)) {
                return true;
            }
        }
        return false;
    }
public:
    int numSquares(int n) {
        square_nums = unordered_set<int>();
        for (int i = 1; i * i <= n; i++) {
            square_nums.insert(i * i);
        }
        for (int count = 1; count <= n; count++) {
            if (is_reachable(n, count)) {
                return count;
            }
        }
        return n;
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
	return solution.numSquares(n);
}
