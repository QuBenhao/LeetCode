//go:build ignore
#include "cpp/common/Solution.h"
#include <queue>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = static_cast<int>(grid.size()), n = static_cast<int>(grid[0].size());
        queue<pair<int, int>> q;
        int fresh = 0, time = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) {
                    q.push({i, j});
                } else if (grid[i][j] == 1) {
                    fresh++;
                }
            }
        }
        if (fresh == 0) {
            return 0;
        }
        vector<pair<int, int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        while (!q.empty()) {
            int size = static_cast<int>(q.size());
            for (int i = 0; i < size; i++) {
                auto [x, y] = q.front();
                q.pop();
                for (auto& dir : dirs) {
                    int nx = x + dir.first, ny = y + dir.second;
                    if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 1) {
                        grid[nx][ny] = 2;
                        q.push({nx, ny});
                        fresh--;
                    }
                }
            }
            time++;
        }
        return fresh == 0 ? time - 1 : -1;
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
	vector<vector<int>> grid = json::parse(inputArray.at(0));
	return solution.orangesRotting(grid);
}
