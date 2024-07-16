//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int numberOfSets(int n, int maxDistance, vector<vector<int>> &roads) {
        vector<vector<int>> g(n, vector<int>(n, INT_MAX / 2)); // 防止加法溢出
        for (int i = 0; i < n; i++) {
            g[i][i] = 0;
        }
        for (auto &e: roads) {
            int x = e[0], y = e[1], wt = e[2];
            g[x][y] = min(g[x][y], wt);
            g[y][x] = min(g[y][x], wt);
        }

        vector<vector<int>> f(n);
        auto check = [&](int s) -> bool {
            for (int i = 0; i < n; i++) {
                if ((s >> i) & 1) {
                    f[i] = g[i];
                }
            }

            // Floyd
            for (int k = 0; k < n; k++) {
                if (((s >> k) & 1) == 0) continue;
                for (int i = 0; i < n; i++) {
                    if (((s >> i) & 1) == 0) continue;
                    for (int j = 0; j < n; j++) {
                        f[i][j] = min(f[i][j], f[i][k] + f[k][j]);
                    }
                }
            }

            for (int i = 0; i < n; i++) {
                if (((s >> i) & 1) == 0) continue;
                for (int j = 0; j < n; j++) {
                    if ((s >> j) & 1 && f[i][j] > maxDistance) {
                        return false;
                    }
                }
            }
            return true;
        };

        int ans = 0;
        for (int s = 0; s < (1 << n); s++) { // 枚举子集
            ans += check(s);
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
	int n = json::parse(inputArray.at(0));
	int maxDistance = json::parse(inputArray.at(1));
	vector<vector<int>> roads = json::parse(inputArray.at(2));
	return solution.numberOfSets(n, maxDistance, roads);
}
