//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_set>
#include <queue>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int openLock(vector<string> &deadends, string target) {
    unordered_set<string> dead(deadends.begin(), deadends.end());
    if (dead.count("0000"))
      return -1;
    if (target == "0000")
      return 0;
    queue<string> q{{"0000"}};
    unordered_set<string> visited{"0000"};
    int res = 0;
    while (!q.empty()) {
      ++res;
      for (int i = q.size(); i > 0; --i) {
        string t = q.front();
        q.pop();
        for (int j = 0; j < 4; ++j) {
          for (int k = -1; k <= 1; k += 2) {
            string s = t;
            s[j] = (s[j] - '0' + k + 10) % 10 + '0';
            if (s == target)
              return res;
            if (dead.count(s) || visited.count(s))
              continue;
            q.push(s);
            visited.insert(s);
          }
        }
      }
    }
    return -1;
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
  vector<string> deadends = json::parse(inputArray.at(0));
  string target = json::parse(inputArray.at(1));
  return solution.openLock(deadends, target);
}
