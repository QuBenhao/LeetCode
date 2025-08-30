//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

constexpr int N = 9;

class Solution {
public:
  bool isValidSudoku(const vector<vector<char>> &board) {
    for (int i = 0; i < N; ++i) {
      int r = 0, c = 0, b = 0;
      for (int j = 0; j < N; ++j) {
        if (board[i][j] != '.') {
          int v = 1 << (board[i][j] - '1');
          if (r & v)
            return false;
          r |= v;
        }
        if (board[j][i] != '.') {
          int v = 1 << (board[j][i] - '1');
          if (c & v)
            return false;
          c |= v;
        }
        int bi = (i / 3) * 3 + j / 3;
        int bj = (i % 3) * 3 + j % 3;
        if (board[bi][bj] != '.') {
          int v = 1 << (board[bi][bj] - '1');
          if (b & v)
            return false;
          b |= v;
        }
      }
    }
    return true;
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
  for (size_t i = 0; i < board.size(); ++i) {
    for (size_t j = 0; j < board[i].size(); ++j) {
      board[i][j] = board_str[i][j][0];
    }
  }
  return solution.isValidSudoku(board);
}
