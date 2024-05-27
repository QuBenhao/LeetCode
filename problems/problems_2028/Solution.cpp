//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
		int remain = mean * (rolls.size() + n) - reduce(rolls.begin(), rolls.end());
		if (remain < n || remain > 6 * n) return {};
		int avg = remain / n, extra = remain % n;
		vector<int> ans(extra, avg + 1);
		ans.insert(ans.end(), n - extra, avg);
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
	vector<int> rolls = json::parse(inputArray.at(0));
	int mean = json::parse(inputArray.at(1));
	int n = json::parse(inputArray.at(2));
	return solution.missingRolls(rolls, mean, n);
}
