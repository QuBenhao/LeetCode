//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  bool searchMatrix(vector<vector<int>> &matrix, int target) {
    int m = static_cast<int>(matrix.size()),
        n = static_cast<int>(matrix[0].size());
    int row = 0, col = n - 1;
    while (row < m && col >= 0) {
      if (matrix[row][col] == target) {
        return true;
      } else if (matrix[row][col] > target) {
        col--;
      } else {
        row++;
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
  vector<vector<int>> matrix = json::parse(inputArray.at(0));
  int target = json::parse(inputArray.at(1));
  return solution.searchMatrix(matrix, target);
}
