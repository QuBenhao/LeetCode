//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

#define MAXN ((int)1e5)
bool flag[MAXN + 5], inited = false;
void init() {
  if (inited)
    return;
  inited = true;
  flag[0] = flag[1] = true;
  // 筛法求质数
  for (int i = 2; i * i <= MAXN; i++) {
    if (!flag[i]) {
      for (int j = i * 2; j <= MAXN; j += i) {
        flag[j] = true;
      }
    }
  }
}

class Solution {
public:
  long long splitArray(const vector<int> &nums) {
    init();
    int64_t ans = 0;
    for (int i = 0; i < nums.size(); ++i) {
      if (flag[i]) {
        ans += nums[i];
      } else {
        ans -= nums[i];
      }
    }
    return ans > 0 ? ans : -ans;
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
  return solution.splitArray(nums);
}
