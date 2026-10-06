//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long distinctNames(vector<string> &ideas) {
    unordered_set<string> groups[26];
    for (auto &s : ideas) {
      groups[s[0] - 'a'].insert(s.substr(1));  // Group by first letter
    }

    int64_t ans = 0;
    for (int a = 1; a < 26; a++) {  // Enumerate all pairs of groups
      for (int b = 0; b < a; b++) {
        int m = 0;  // Size of the intersection
        for (auto &s : groups[a]) {
          m += groups[b].count(s);
        }
        ans += (int64_t)(groups[a].size() - m) * (groups[b].size() - m);
      }
    }
    return ans * 2;  // Multiply by 2 at the end
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
