//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  string customSortString(string order, string s) {
    array<int, 26> count{0};
    for (char c : s) {
      ++count[c - 'a'];
    }
    string result;
    for (char c : order) {
      if (count[c - 'a'] > 0) {
        result.append(count[c - 'a'], c);
        count[c - 'a'] = 0; // Reset count to avoid duplicates
      }
    }
    for (int i = 0; i < 26; ++i) {
      if (count[i] > 0) {
        result.append(count[i], 'a' + i);
      }
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
  string order = json::parse(inputArray.at(0));
  string s = json::parse(inputArray.at(1));
  return solution.customSortString(order, s);
}
