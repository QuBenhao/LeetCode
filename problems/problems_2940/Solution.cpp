//go:build ignore
#include "cpp/common/Solution.h"
#include <queue>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> leftmostBuildingQueries(vector<int>& heights, vector<vector<int>>& queries) {
        vector<int> ans(queries.size(), -1);
        vector<vector<pair<int, int>>> qs(heights.size());
        for (int i = 0; i < queries.size(); i++) {
            int a = queries[i][0], b = queries[i][1];
            if (a > b) {
                swap(a, b); // 保证 a <= b
            }
            if (a == b || heights[a] < heights[b]) {
                ans[i] = b; // i 直接跳到 j
            } else {
                qs[b].emplace_back(heights[a], i); // 离线询问
            }
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        for (int i = 0; i < heights.size(); i++) {
            while (!pq.empty() && pq.top().first < heights[i]) {
                // 堆顶的 heights[a] 可以跳到 heights[i]
                ans[pq.top().second] = i;
                pq.pop();
            }
            for (auto& p : qs[i]) {
                pq.emplace(p); // 后面再回答
            }
        }
        return ans;
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
	vector<int> heights = json::parse(inputArray.at(0));
	vector<vector<int>> queries = json::parse(inputArray.at(1));
	return solution.leftmostBuildingQueries(heights, queries);
}
