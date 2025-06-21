//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maxTurbulenceSize(vector<int> &arr) {
    int n = arr.size(), ans = 1;
    int cur0 = 1, cur1 = 1;
    for (int i = 1; i < n; ++i) {
      if (arr[i] > arr[i - 1]) {
        cur1 = cur0 + 1;
        cur0 = 1;
      } else if (arr[i] < arr[i - 1]) {
        cur0 = cur1 + 1;
        cur1 = 1;
      } else {
        cur0 = 1;
        cur1 = 1;
      }
      ans = max(ans, max(cur0, cur1));
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
  vector<int> arr = json::parse(inputArray.at(0));
  return solution.maxTurbulenceSize(arr);
}
