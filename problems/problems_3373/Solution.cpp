//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
    int dfs(const vector<vector<int>>& graph, int node, int parent, int d) {
        int ans = d == 0 ? 1 : 0;
        for (auto neigh: graph[node]) {
            if (neigh == parent) {
                continue;
            }
            ans += dfs(graph, neigh, node, d ^ 1);
        }
        return ans;
    }

    void dfs2(const vector<vector<int>>& graph, int node, int parent, vector<int>& ans, int m, int max2) {
        for (auto neigh: graph[node]) {
            if (neigh == parent) {
                continue;
            }
            ans[neigh] = m - ans[node] + max2 * 2;
            dfs2(graph, neigh, node, ans, m, max2);
        }
    }
public:
    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
        auto buildGraph = [&](const vector<vector<int>>& edges) {
            vector<vector<int>> graph(edges.size() + 1);
            for (const auto& edge : edges) {
                graph[edge[0]].push_back(edge[1]);
                graph[edge[1]].push_back(edge[0]);
            }
            return graph;
        };

        auto graph1 = buildGraph(edges1);
        auto graph2 = buildGraph(edges2);
        int m = static_cast<int>(graph1.size()), n = static_cast<int>(graph2.size());
        int a = dfs(graph2, 0, -1, 1);
        int max2 = max(a, n - a);
        vector<int> ans(m, 0);
        ans[0] = dfs(graph1, 0, -1, 0) + max2;
        dfs2(graph1, 0, -1, ans, m, max2);
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
	vector<vector<int>> edges1 = json::parse(inputArray.at(0));
	vector<vector<int>> edges2 = json::parse(inputArray.at(1));
	return solution.maxTargetNodes(edges1, edges2);
}
