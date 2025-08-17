//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minSensors(int n, int m, int k) {
    k = 2 * k + 1;
    return ((m - 1) / k + 1) * ((n - 1) / k + 1);
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
  int n = json::parse(inputArray.at(0));
  int m = json::parse(inputArray.at(1));
  int k = json::parse(inputArray.at(2));
  return solution.minSensors(n, m, k);
}
