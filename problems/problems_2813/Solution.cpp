//go:build ignore
#include "cpp/common/Solution.h"
#include <ranges>
#include <unordered_set>
#include <stack>
#include <algorithm>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    long long findMaximumElegance(vector<vector<int>>& items, int k) {
        ranges::sort(items, [](const auto& a, const auto&b) {return a[0] > b[0];});
        long long ans = 0LL, total_profit = 0LL;
        unordered_set<int> vis;
        stack<int> duplicate;
        for (int i = 0; i < items.size(); i++) {
            int profit = items[i][0], category = items[i][1];
            if (i < k) {
                total_profit += profit;
                if (vis.find(category) == vis.end()) {
                    vis.insert(category);
                } else {
                    duplicate.push(profit);
                }
            } else if (!duplicate.empty() && vis.find(category) == vis.end()) {
                total_profit += profit - duplicate.top();
                vis.insert(category);
                duplicate.pop();
            }
            ans = max(ans, total_profit + (long long)vis.size() * (long long)vis.size());
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
	vector<vector<int>> items = json::parse(inputArray.at(0));
	int k = json::parse(inputArray.at(1));
	return solution.findMaximumElegance(items, k);
}
