//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int numOfUnplacedFruits(const vector<int> &fruits, vector<int> &baskets) {
    int ans = 0;
    int n = baskets.size();
    for (const auto &fruit : fruits) {
      int i = 0;
      while (i < n && baskets[i] < fruit) {
        ++i;
      }
      if (i == n) {
        ++ans;
      } else {
        baskets[i] = 0;
      }
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
  vector<int> fruits = json::parse(inputArray.at(0));
  vector<int> baskets = json::parse(inputArray.at(1));
  return solution.numOfUnplacedFruits(fruits, baskets);
}
