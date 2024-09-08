//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_map>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int lengthOfLongestSubstring(string s) {
    int n = static_cast<int>(s.size());
    int ans = 0;
    unordered_map<char, bool> map;
    for (int left = 0, right = 0; right < n; right++) {
      while (map.find(s[right]) != map.end()) {
        map.erase(s[left]);
        left++;
      }
      map[s[right]] = true;
      ans = max(ans, right - left + 1);
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
  return solution.lengthOfLongestSubstring(s);
}
