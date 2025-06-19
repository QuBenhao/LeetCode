//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maxDistance(string s, int k) {
    int n = s.size(), x = 0, y = 0;
    k *= 2;
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      switch (s[i]) {
      case 'N':
        ++y;
        break;
      case 'S':
        --y;
        break;
      case 'E':
        ++x;
        break;
      case 'W':
        --x;
        break;
      }
      ans = max(ans, min(i+1, k + abs(x) + abs(y)));
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
  string s = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  return solution.maxDistance(s, k);
}
