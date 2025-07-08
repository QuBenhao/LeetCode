//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  bool canTransform(const string& start, const string& result) {
    int l = 0, r = 0;
    int n = start.size();
    for (int i = 0; i < n; ++i) {
      if ((start[i] == 'L' && r > 0) || (start[i] == 'R' && l < 0)) {
        return false;
      }
      l += start[i] == 'L' ? 1 : 0;
      r += start[i] == 'R' ? 1 : 0;
      l -= result[i] == 'L' ? 1 : 0;
      r -= result[i] == 'R' ? 1 : 0;
      if ((l != 0 && r != 0) || l > 0 || r < 0) {
        return false;
      }
    }
    return l == 0 && r == 0;
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
  string start = json::parse(inputArray.at(0));
  string result = json::parse(inputArray.at(1));
  return solution.canTransform(start, result);
}
