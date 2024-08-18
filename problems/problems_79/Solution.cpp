//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
private:
  static constexpr int directions[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

public:
  bool exist(vector<vector<char>> &board, string word) {
    int m = static_cast<int>(board.size()),
        n = static_cast<int>(board[0].size()),
        len = static_cast<int>(word.size());
    function<bool(int, int, int)> backtrack = [&](int i, int j, int k) -> bool {
      if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] != word[k]) {
        return false;
      }
      if (k == len - 1) {
        return true;
      }
      char tmp = board[i][j];
      board[i][j] = '\0';
      for (auto dir : directions) {
        if (backtrack(i + dir[0], j + dir[1], k + 1)) {
          return true;
        }
      }
      board[i][j] = tmp;
      return false;
    };

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (backtrack(i, j, 0)) {
          return true;
        }
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
  auto board =
      vector<vector<char>>(board_str.size(), vector<char>(board_str[0].size()));
  for (int i = 0; i < board.size(); i++) {
    for (int j = 0; j < board[i].size(); j++) {
      board[i][j] = board_str[i][j][0];
    }
  }
  string word = json::parse(inputArray.at(1));
  return solution.exist(board, word);
}
