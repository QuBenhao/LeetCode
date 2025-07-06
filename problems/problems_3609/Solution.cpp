//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minMoves(int sx, int sy, int tx, int ty) {
    if (sx == tx && sy == ty) {
      return 0;
    }
    if (sx > tx || sy > ty) {
      return -1;
    }
    int ans;
    if (tx == ty) {
      if (sx == 0) {
        swap(sx, sy);
        swap(tx, ty);
      }
      ans = minMoves(sx, sy, tx, 0);
    } else {
      if (tx < ty) {
        swap(sx, sy);
        swap(tx, ty);
      }
      if (tx > ty * 2) {
        if (tx & 1) {
          return -1;
        }
        ans = minMoves(sx, sy, tx / 2, ty);
      } else {
        ans = minMoves(sx, sy, tx - ty, ty);
      }
    }
    return ans == -1 ? -1 : ans + 1;
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
  int sx = json::parse(inputArray.at(0));
  int sy = json::parse(inputArray.at(1));
  int tx = json::parse(inputArray.at(2));
  int ty = json::parse(inputArray.at(3));
  return solution.minMoves(sx, sy, tx, ty);
}
