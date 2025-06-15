//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int largestAltitude(vector<int> &gain) {
    int maxAltitude = 0;
    int cur = 0;
    for (const auto g : gain) {
      cur += g;
      if (cur > maxAltitude) {
        maxAltitude = cur;
      }
    }
    return maxAltitude;
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
  vector<int> gain = json::parse(inputArray.at(0));
  return solution.largestAltitude(gain);
}
