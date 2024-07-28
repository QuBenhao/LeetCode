//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>


using namespace std;
using json = nlohmann::json;

class Solution {
private:
    void dfs(vector<vector<int>>& res, vector<int>& candidates, vector<int>& path, int target, int index) {
        if (target == 0) {
            res.emplace_back(path);
            return;
        }
        if (index == candidates.size()) {
            return;
        }
        if (candidates[index] <= target) {
            path.emplace_back(candidates[index]);
            dfs(res, candidates, path, target - candidates[index], index);
            path.pop_back();
        }
        dfs(res, candidates, path, target, index + 1);
    }
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> path;
        dfs(res, candidates, path, target, 0);
        return res;
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
	vector<int> candidates = json::parse(inputArray.at(0));
	int target = json::parse(inputArray.at(1));
	return solution.combinationSum(candidates, target);
}
