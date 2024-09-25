//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long distinctNames(vector<string> &ideas) {
    unordered_set<string> groups[26];
    for (auto &s : ideas) {
      groups[s[0] - 'a'].insert(s.substr(1));  // 按照首字母分组
    }

    int64_t ans = 0;
    for (int a = 1; a < 26; a++) {  // 枚举所有组对
      for (int b = 0; b < a; b++) {
        int m = 0;  // 交集的大小
        for (auto &s : groups[a]) {
          m += groups[b].count(s);
        }
        ans += (int64_t)(groups[a].size() - m) * (groups[b].size() - m);
      }
    }
    return ans * 2;  // 乘 2 放到最后
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
  vector<string> ideas = json::parse(inputArray.at(0));
  return solution.distinctNames(ideas);
}
