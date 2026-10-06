//go:build ignore
#include "cpp/common/Solution.h"
#include <queue>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maximalPathQuality(vector<int>& values, vector<vector<int>>& edges, int max_time) {
        int n = values.size();
        vector<vector<pair<int, int>>> g(n);
        for (auto& e : edges) {
            int x = e[0], y = e[1], t = e[2];
            g[x].emplace_back(y, t);
            g[y].emplace_back(x, t);
        }

        // Dijkstra's algorithm
        vector<int> dis(n, INT_MAX);
        dis[0] = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        pq.emplace(0, 0);
        while (!pq.empty()) {
            auto [dx, x] = pq.top();
            pq.pop();
            if (dx > dis[x]) { // x was already popped from the heap
                continue;
            }
            for (auto& [y, d] : g[x]) {
                int new_dis = dx + d;
                if (new_dis < dis[y]) {
                    dis[y] = new_dis; // Update the shortest distances to x's neighbors
                    pq.emplace(new_dis, y);
                }
            }
        }

        int ans = 0;
        vector<int> vis(n);
        vis[0] = true;
        auto dfs = [&](auto&& self, int x, int sum_time, int sum_value) -> void {
            if (x == 0) {
                ans = max(ans, sum_value);
                // Do not return here; the walk can continue
            }
            for (auto& [y, t] : g[x]) {
                // Compared with method 1, this also includes dis[y]
                if (sum_time + t + dis[y] > max_time) {
                    continue;
                }
                if (vis[y]) {
                    self(self, y, sum_time + t, sum_value);
                } else {
                    vis[y] = true;
                    // Count each node's value at most once in the total
                    self(self, y, sum_time + t, sum_value + values[y]);
                    vis[y] = false; // Restore the previous state
                }
            }
        };
        dfs(dfs, 0, 0, values[0]);
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
	vector<int> values = json::parse(inputArray.at(0));
	vector<vector<int>> edges = json::parse(inputArray.at(1));
	int maxTime = json::parse(inputArray.at(2));
	return solution.maximalPathQuality(values, edges, maxTime);
}
