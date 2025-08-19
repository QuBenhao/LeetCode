//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int uniqueLetterString(const string &s) {
    unordered_map<char, vector<int>> charIndices;
    int n = s.size();
    for (int i = 0; i < n; ++i) {
      charIndices[s[i]].push_back(i);
    }

    int ans = 0;
    for (const auto &[_, indices] : charIndices) {
      int m = indices.size();
      if (m == 0) {
        continue;
      }
      if (m == 1) {
        ans += (indices[0] + 1) * (n - indices[0]);
        continue;
      }
      for (int i = 0; i < m; ++i) {
        if (i == 0) {
          ans += (indices[i] + 1) * (indices[i + 1] - indices[i]);
        } else if (i == m - 1) {
          ans += (n - indices[i]) * (indices[i] - indices[i - 1]);
        } else {
          ans +=
              (indices[i] - indices[i - 1]) * (indices[i + 1] - indices[i]);
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
  string s = json::parse(inputArray.at(0));
  return solution.uniqueLetterString(s);
}
