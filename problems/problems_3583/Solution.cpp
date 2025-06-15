//go:build ignore
#include "cpp/common/Solution.h"

#include <unordered_map>

using namespace std;
using json = nlohmann::json;

static const int MOD = 1e9 + 7;
class Solution {
public:
  int specialTriplets(vector<int> &nums) {
    int n = nums.size();
    unordered_map<int, int> prefixCount, suffixCount;
    for (auto num : nums) {
      suffixCount[num]++;
    }
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      suffixCount[nums[i]]--;
      ans = (ans + 1LL * prefixCount[nums[i] * 2] * suffixCount[nums[i] * 2] % MOD) % MOD;
      prefixCount[nums[i]]++;
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
  return solution.specialTriplets(nums);
}
