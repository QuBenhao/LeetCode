//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int areaOfMaxDiagonal(const vector<vector<int>> &dimensions) {
    int max_length = 0, max_area = 0;
    for (const auto &dim : dimensions) {
      int a = dim[0], b = dim[1];
      int length = a * a + b * b;
      if (length > max_length) {
        max_length = length;
        max_area = a * b;
      } else if (length == max_length) {
        max_area = max(max_area, a * b);
      }
    }
    return max_area;
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
  vector<vector<int>> dimensions = json::parse(inputArray.at(0));
  return solution.areaOfMaxDiagonal(dimensions);
}
