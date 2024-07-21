//go:build ignore
#include "cpp/common/Solution.h"
#include <queue>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maximumDetonation(vector<vector<int>>& bombs) {
        auto n = static_cast<int>(bombs.size());
        auto graph = vector<vector<int>>(n);
        for (int i = 0; i < n - 1; i++) {
            long long x1 = bombs[i][0], y1 = bombs[i][1], r1 = bombs[i][2];
            r1 *= r1;
            for (int j = i + 1; j < n; j++) {
                long long x2 = bombs[j][0], y2 = bombs[j][1], r2 = bombs[j][2];
                r2 *= r2;
                long long d = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
                if (d <= r1) {
                    graph[i].push_back(j);
                }
                if (d <= r2) {
                    graph[j].push_back(i);
                }
            }
        }
        auto ans = 0;
        for (int i = 0; i < n; i++) {
            auto cur = 0;
            auto visited = vector<bool>(n);
            auto q = queue<int>();
            q.push(i);
            visited[i] = true;
            while (!q.empty()) {
                auto u = q.front();
                q.pop();
                cur++;
                for (auto v: graph[u]) {
                    if (!visited[v]) {
                        visited[v] = true;
                        q.push(v);
                    }
                }
            }
            ans = max(ans, cur);
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
	vector<vector<int>> bombs = json::parse(inputArray.at(0));
	return solution.maximumDetonation(bombs);
}
