//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int findLucky(const vector<int> &arr) {
    unordered_map<int, int> count_map;
    for (int num : arr) {
      ++count_map[num];
    }
    int ans = -1;
    for (const auto &[num, count] : count_map) {
      if (num == count) {
        ans = max(ans, num);
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
  vector<int> arr = json::parse(inputArray.at(0));
  return solution.findLucky(arr);
}
