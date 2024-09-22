//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_map>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int subarraySum(vector<int> &nums, int k) {
    int ans = 0, s = 0, n = static_cast<int>(nums.size());
    unordered_map<int, int> mp;
    mp[0] = 1;
    for (int i = 0; i < n; i++) {
      s += nums[i];
      if (mp.find(s - k) != mp.end()) {
        ans += mp[s - k];
      }
      mp[s]++;
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
  vector<int> nums = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  return solution.subarraySum(nums, k);
}
