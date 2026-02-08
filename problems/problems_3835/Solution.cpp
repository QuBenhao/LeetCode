//go:build ignore
#include "cpp/common/Solution.h"
#include <deque>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long countSubarrays(vector<int> &nums, long long k) {
    long long ans = 0LL;
    std::deque<int> max_queue, min_queue;
    int i = 0, n = nums.size();
    for (int j = 0; j < n; ++j) {
      while (!max_queue.empty() && nums[max_queue.back()] <= nums[j])
        max_queue.pop_back();
      max_queue.emplace_back(j);
      while (!min_queue.empty() && nums[min_queue.back()] >= nums[j])
        min_queue.pop_back();
      min_queue.emplace_back(j);

      while (i < j &&  (1LL + j - i) * (nums[max_queue.front()] - nums[min_queue.front()]) > k) {
        ++i;
        if (max_queue.front() < i)
          max_queue.pop_front();
        if (min_queue.front() < i)
          min_queue.pop_front();
      }
      ans += j - i + 1;
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
  long long k = json::parse(inputArray.at(1));
  return solution.countSubarrays(nums, k);
}
