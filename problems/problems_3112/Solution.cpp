//go:build ignore
#include "cpp/common/Solution.h"
#include <queue>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> minimumTime(int n, vector<vector<int>>& edges, vector<int>& disappear) {
        vector<vector<pair<int, int>>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].emplace_back(edge[1], edge[2]);
            graph[edge[1]].emplace_back(edge[0], edge[2]);
        }
        vector<int> dis(n, -1);
        dis[0] = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        pq.emplace(0, 0);
        while (!pq.empty()) {
            auto [d, u] = pq.top();
            pq.pop();
            if (dis[u] < d) {
                continue;
            }
            for (auto& [v, w] : graph[u]) {
                if (auto new_dis = d + w; new_dis < disappear[v] && (dis[v] == -1 || new_dis < dis[v])) {
                    dis[v] = new_dis;
                    pq.emplace(new_dis, v);
                }
            }
        }
        return dis;
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
	vector<vector<int>> edges = json::parse(inputArray.at(1));
	vector<int> disappear = json::parse(inputArray.at(2));
	return solution.minimumTime(n, edges, disappear);
}
