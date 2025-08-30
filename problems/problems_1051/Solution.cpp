//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int heightChecker(const vector<int> &heights) {
    vector<int> expected = heights;
    sort(expected.begin(), expected.end());
    int moves = 0;
    for (int i = 0; i < heights.size(); i++) {
      if (heights[i] != expected[i]) {
        moves++;
      }
    }
    return moves;
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
  vector<int> heights = json::parse(inputArray.at(0));
  return solution.heightChecker(heights);
}
