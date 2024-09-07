//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int lenLongestFibSubseq(vector<int> &arr) {
    int n = static_cast<int>(arr.size());
    unordered_map<int, int> index;
    for (int i = 0; i < n; i++) {
      index[arr[i]] = i;
    }
    int ans = 0;
    unordered_map<int, unordered_map<int, int>> dp;
    for (int i = 0; i < n - 1; i++) {
      for (int j = i + 1; j < n; j++) {
        int nxt = arr[i] + arr[j];
        if (index.find(nxt) != index.end()) {
          int k = index[nxt];
          dp[j][k] = dp[i][j] + 1;
          ans = max(ans, dp[j][k] + 2);
        }
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
  return solution.lenLongestFibSubseq(arr);
}
