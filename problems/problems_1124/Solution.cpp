//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int longestWPI(const vector<int> &hours) {
    int n = hours.size();
    int max_length = 0;
    int prefix_sum = 0;
    unordered_map<int, int> prefix_sum_index;
    for (int i = 0; i < n; ++i) {
      prefix_sum += hours[i] > 8 ? 1 : -1;
      if (prefix_sum_index.find(prefix_sum) == prefix_sum_index.end()) {
        prefix_sum_index[prefix_sum] = i;
      }
      if (prefix_sum > 0) {
        max_length = i + 1;
      } else {
        // Check for a prefix sum that is one less
        // as prefix_sum - x must come after prefix_sum - 1
        auto it = prefix_sum_index.find(prefix_sum - 1);
        if (it != prefix_sum_index.end()) {
          max_length = max(max_length, i - it->second);
        }
      }
    }
    return max_length;
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
  vector<int> hours = json::parse(inputArray.at(0));
  return solution.longestWPI(hours);
}
