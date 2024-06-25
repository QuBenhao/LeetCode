//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_map>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    bool confusingNumber(int n) {
        auto trans = unordered_map<int, int>({{0, 0}, {1, 1}, {6, 9}, {8, 8}, {9, 6}});
        int revert = 0;
        for (int num = n; num > 0; num /= 10) {
            int cur = num % 10;
            if (trans.find(cur) == trans.end()) {
                return false;
            }
            revert = 10 * revert + trans[cur];
        }
        return revert != n;
    }
};

json leetcode::qubh::Solve(string input) {
	vector<string> inputArray;
	size_t pos = input.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find('\n');
	}
	inputArray.push_back(input);

	Solution solution;
	int n = json::parse(inputArray.at(0));
	return solution.confusingNumber(n);
}
