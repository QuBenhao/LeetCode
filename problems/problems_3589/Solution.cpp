//go:build ignore
#include "cpp/common/Solution.h"

#include <deque>

using namespace std;
using json = nlohmann::json;

#define MAXN ((int)5e4)
bool inited = false, is_prime[MAXN + 1];
void init() {
  if (inited)
    return;
  inited = true;
  fill(is_prime, is_prime + MAXN + 1, true);
  is_prime[0] = is_prime[1] = false;
  for (int i = 2; i * i <= MAXN; ++i) {
    if (is_prime[i]) {
      for (int j = i * i; j <= MAXN; j += i) {
        is_prime[j] = false;
      }
    }
  }
}

class Solution {
public:
  int primeSubarray(vector<int> &nums, int k) {
    init();
    deque<int> q, max_q, min_q;
    int n = nums.size(), ans = 0, left = 0;
    for (int right = 0; right < n; ++right) {
      int num = nums[right];
      if (is_prime[num]) {
        q.push_back(right);
        while (!max_q.empty() && nums[max_q.back()] <= num) {
          max_q.pop_back();
        }
        max_q.push_back(right);
        while (!min_q.empty() && nums[min_q.back()] >= num) {
          min_q.pop_back();
        }
        min_q.push_back(right);
      }
      while (!q.empty() && (nums[max_q.front()] - nums[min_q.front()] > k)) {
        left = q.front() + 1;
        q.pop_front();
        while (!max_q.empty() && max_q.front() < left) {
          max_q.pop_front();
        }
        while (!min_q.empty() && min_q.front() < left) {
          min_q.pop_front();
        }
      }
      if (q.size() > 1) {
        int tmp = q.back();
        q.pop_back();
        ans += q.back() - left + 1;
        q.push_back(tmp);
      }
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
  return solution.primeSubarray(nums, k);
}
