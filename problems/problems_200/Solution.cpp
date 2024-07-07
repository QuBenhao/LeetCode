//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int numIslands(vector<vector<char>> &grid) {
        auto m = grid.size(), n = grid[0].size();
        int ans = 0;
        for (auto i = 0; i < m; i++) {
            for (auto j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    ans++;
                    dfs(grid, i, j);
                }
            }
        }
        return ans;
    }

private:
    vector<vector<int>> directions = {{0,  1},
                                      {0,  -1},
                                      {1,  0},
                                      {-1, 0}};

    void dfs(vector<vector<char>> &grid, int i, int j) {
        auto m = grid.size(), n = grid[0].size();
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == '0') return;
        grid[i][j] = '0';
        for (auto dir: directions) {
            dfs(grid, i + dir[0], j + dir[1]);
        }
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
    vector<vector<string>> grid_str = json::parse(inputArray.at(0));
    auto grid = vector<vector<char>>(grid_str.size(), vector<char>(grid_str[0].size()));
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[i].size(); j++) {
            grid[i][j] = grid_str[i][j][0];
        }
    }
    return solution.numIslands(grid);
}
