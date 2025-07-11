//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> constructArray(int n, int k) {
    vector<int> result;
    for (int i = 0; i < k + 1; ++i) {
      if (i % 2 == 0) {
        result.push_back(i / 2 + 1);
      } else {
        result.push_back(k - i / 2 + 1);
      }
    }
    for (int i = k + 2; i <= n; ++i) {
      result.push_back(i);
    }
    return result;
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
  int k = json::parse(inputArray.at(1));
  return solution.constructArray(n, k);
}
