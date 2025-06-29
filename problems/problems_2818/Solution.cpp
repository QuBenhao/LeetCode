//go:build ignore
#include "cpp/common/Solution.h"

#include <stack>

using namespace std;
using json = nlohmann::json;

const int MOD = 1000000007;
#define MAX_N 100001

vector<int> omega(MAX_N);
bool inited = false;
void init() {
  if (inited)
    return;
  inited = true;
  for (int i = 2; i < MAX_N; ++i) {
    if (omega[i] == 0) {
      for (int j = i; j < MAX_N; j += i) {
        ++omega[j];
      }
    }
  }
}

class Solution {
  int fast_pow(int64_t a, int64_t b) {
    int64_t res = 1;
    while (b > 0) {
      if (b & 1) {
        res = res * a % MOD;
      }
      a = a * a % MOD;
      b >>= 1;
    }
    return res;
  }

public:
  int maximumScore(vector<int> &nums, int k) {
    init();
    int n = nums.size();
    vector<int> cnt(n, 0);
    for (int i = 0; i < n; ++i) {
      cnt[i] = omega[nums[i]];
    }
    vector<int> left(n, -1), right(n, n);
    stack<int> s;
    for (int i = 0; i < n; ++i) {
      while (!s.empty() && cnt[s.top()] < cnt[i]) {
        right[s.top()] = i;
        s.pop();
      }
      if (!s.empty()) {
        left[i] = s.top();
      }
      s.push(i);
    }
    int64_t ans = 1;
    vector<int> idxes(n);
    iota(idxes.begin(), idxes.end(), 0);
    sort(idxes.begin(), idxes.end(),
         [&](int i, int j) { return nums[i] > nums[j]; });
    for (int i = 0; i < n && k > 0 && nums[idxes[i]] > 1; ++i) {
      int idx = idxes[i];
      int num = nums[idx];
      long long l = left[idx], r = right[idx];
      long long take = min((long long)k, (r - idx) * (idx - l));
      ans = (ans * fast_pow(num, take)) % MOD;
      k -= take;
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
  return solution.maximumScore(nums, k);
}
