//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<int> cnt(n * n + 1);
        for (auto& row : grid) {
            for (int x : row) {
                cnt[x]++;
            }
        }

        vector<int> ans(2);
        for (int i = 1; i <= n * n; i++) {
            if (cnt[i] == 2) {
                ans[0] = i; // 出现两次的数
            } else if (cnt[i] == 0) {
                ans[1] = i; // 出现零次的数
            }
        }
        return ans;
    }
};

json leetcode::qubh::Solve(string input)
{
	vector<string> inputArray;
	int pos = input.find("\n");
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find("\n");
	}
	inputArray.push_back(input);

	Solution solution;
	vector<vector<int>> grid = json::parse(inputArray.at(0));
	return solution.findMissingAndRepeatedValues(grid);
}
