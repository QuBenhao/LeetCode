//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int ans = 0;
        size_t n = mat.size();
        for (int i = 0; i < n; i++) {
            ans += mat[i][i] + mat[i][n - 1 - i];
        }
        if (n % 2 == 1) {
            ans -= mat[n/2][n/2];
        }
        return ans;
    }
};

json leetcode::qubh::Solve(string input)
{
	vector<string> inputArray;
	size_t pos = input.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find('\n');
	}
	inputArray.push_back(input);

	Solution solution;
	vector<vector<int>> mat = json::parse(inputArray.at(0));
	return solution.diagonalSum(mat);
}
