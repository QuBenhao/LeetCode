//go:build ignore
#include "cpp/common/Solution.h"
#include <string>
#include <unordered_map>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minimumOperationsToMakeKPeriodic(string word, int k) {
    unordered_map<string, int> counter;
    int n = static_cast<int>(word.size());
    int ans = 0;
    for (int i = 0; i < n; i += k) {
      string sub = word.substr(i, k);
      counter[sub]++;
      ans = max(ans, counter[sub]);
    }
    return n / k - ans;
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
  string word = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  return solution.minimumOperationsToMakeKPeriodic(word, k);
}
