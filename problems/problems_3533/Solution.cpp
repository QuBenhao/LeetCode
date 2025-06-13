//go:build ignore
#include "cpp/common/Solution.h"
#include "cpp/models/TreeNode.h"

#include <algorithm>
#include <unordered_map>
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
private:
  bool dfs(const vector<int> &nums, const vector<int> &pow10,
           const vector<int> &mods, vector<unordered_map<int, bool>> &cache,
           vector<int> &ans, int n, int k, int s, int x) {
    if (s == 0) {
      return x % k == 0;
    }
    auto it = cache[x].find(s);
    if (it != cache[x].end()) {
      return it->second;
    }
    for (int i = 0; i < n; ++i) {
      if (((s >> i) & 1) == 0) {
        continue;
      }
      int nxt = s ^ (1 << i);
      int newX = (x * pow10[i] + mods[i]) % k;
      if (dfs(nums, pow10, mods, cache, ans, n, k, nxt, newX)) {
        cache[x][s] = true;
        ans.push_back(nums[i]);
        return true;
      }
    }
    cache[x][s] = false;
    return false;
  }

public:
  vector<int> concatenatedDivisibility(vector<int> &nums, int k) {
    int n = nums.size();
    int mask = 1 << n;
    sort(nums.begin(), nums.end());
    vector<int> mods(n);
    vector<int> pow10(n, 1);
    for (int i = 0; i < n; i++) {
      mods[i] = nums[i] % k;
      for (int num = nums[i]; num > 0; num /= 10) {
        pow10[i] = (pow10[i] * 10) % k;
      }
    }
    vector<unordered_map<int, bool>> cache(k, unordered_map<int, bool>());
    vector<int> ans;
    if (dfs(nums, pow10, mods, cache, ans, n, k, mask - 1, 0)) {
      reverse(ans.begin(), ans.end());
      return ans;
    }
    return {};
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
  return solution.concatenatedDivisibility(nums, k);
}
