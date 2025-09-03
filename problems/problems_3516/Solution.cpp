//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int findClosest(int x, int y, int z) {
    int d1 = abs(x - z), d2 = abs(y - z);
    return d1 == d2 ? 0 : (d1 < d2 ? 1 : 2);
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
  int x = json::parse(inputArray.at(0));
  int y = json::parse(inputArray.at(1));
  int z = json::parse(inputArray.at(2));
  return solution.findClosest(x, y, z);
}
