//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    bool checkMove(vector<vector<char>> &board, int rMove, int cMove, char color) {
        auto m = board.size(), n = board[0].size();
        vector<vector<int>> dirs = {{0,  1},
                                    {1,  1},
                                    {1,  0},
                                    {1,  -1},
                                    {0,  -1},
                                    {-1, -1},
                                    {-1, 0},
                                    {-1, 1}};
        for (auto dir: dirs) {
            auto x = rMove + dir[0], y = cMove + dir[1];
            if (x < 0 || x >= m || y < 0 || y >= n || board[x][y] == '.' || board[x][y] == color) continue;
            while (x >= 0 && x < m && y >= 0 && y < n && board[x][y] != '.') {
                if (board[x][y] == color) return true;
                x += dir[0], y += dir[1];
            }
        }
        return false;
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
    vector<vector<string>> board_str = json::parse(inputArray.at(0));
    auto board = vector<vector<char>>(board_str.size(), vector<char>(board_str[0].size()));
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[i].size(); j++) {
            board[i][j] = board_str[i][j][0];
        }
    }
    int rMove = json::parse(inputArray.at(1));
    int cMove = json::parse(inputArray.at(2));
    string color_string = json::parse(inputArray.at(3));
    char color = color_string.length() > 1 ? color_string[1] : color_string[0];
    return solution.checkMove(board, rMove, cMove, color);
}
