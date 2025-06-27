//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long waysToBuyPensPencils(int total, int cost1, int cost2) {
    int64_t ans = 0;
    while (total >= 0) {
      ans += total / cost2 + 1;
      total -= cost1;
    }
    return ans;
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
  int total = json::parse(inputArray.at(0));
  int cost1 = json::parse(inputArray.at(1));
  int cost2 = json::parse(inputArray.at(2));
  return solution.waysToBuyPensPencils(total, cost1, cost2);
}
