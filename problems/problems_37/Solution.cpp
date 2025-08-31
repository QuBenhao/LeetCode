//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

constexpr int N = 9;

class Solution {
public:
  void solveSudoku(vector<vector<char>> &board) {
    array<int, N> rows{}, cols{}, boxes{};
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < N; ++j) {
        if (board[i][j] != '.') {
          rows[i] |= 1 << (board[i][j] - '1');
          cols[j] |= 1 << (board[i][j] - '1');
          boxes[(i / 3) * 3 + (j / 3)] |= 1 << (board[i][j] - '1');
        }
      }
    }
    auto backtrack = [&board, &rows, &cols, &boxes](this auto &&backtrack,
                                                    int i, int j) -> bool {
      if (i == N)
        return true;
      if (j == N)
        return backtrack(i + 1, 0);
      if (board[i][j] != '.')
        return backtrack(i, j + 1);
      for (char c = '1'; c <= '9'; ++c) {
        int v = 1 << (c - '1');
        int boxI = (i / 3) * 3 + (j / 3);
        if ((rows[i] & v) || (cols[j] & v) || (boxes[boxI] & v))
          continue;
        board[i][j] = c;
        rows[i] |= v;
        cols[j] |= v;
        boxes[boxI] |= v;
        if (backtrack(i, j + 1))
          return true;
        board[i][j] = '.';
        rows[i] &= ~v;
        cols[j] &= ~v;
        boxes[boxI] &= ~v;
      }
      return false;
    };

    backtrack(0, 0);
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
  solution.solveSudoku(board);
  return board;
}
