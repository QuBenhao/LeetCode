//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int findWinningPlayer(vector<int> &skills, int k) {
    int ans = 0, cur = 0, n = static_cast<int>(skills.size());
    for (int i = 1; i < n; i++) {
      if (skills[i] < skills[ans]) {
        cur++;
      } else {
        cur = 1;
        ans = i;
      }
      if (cur == k) {
        break;
      }
    }
    return ans;
  };
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
  vector<int> skills = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  return solution.findWinningPlayer(skills, k);
}
