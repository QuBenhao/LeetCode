//go:build ignore
#include "cpp/common/Solution.h"

#include <cstdint>
#include <numeric>
#include <queue>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long minimumDifference(const vector<int> &nums) {
    int n = nums.size() / 3;
    priority_queue<int, vector<int>, greater<int>> minHeap(nums.end() - n, nums.end());
    int64_t suffixSum = reduce(nums.end() - n, nums.end(), 0LL);
    vector<int64_t> suffixMax(n + 1);
    suffixMax[n] = suffixSum;
    for (int i = 2 * n - 1; i >= n; --i) {
      minHeap.push(nums[i]);
      suffixSum += nums[i] - minHeap.top();
      minHeap.pop();
      suffixMax[i - n] = suffixSum;
    }
    priority_queue<int> maxHeap(nums.begin(), nums.begin() + n);
    int64_t prefixSum = reduce(nums.begin(), nums.begin() + n, 0LL);
    int64_t ans = prefixSum - suffixMax[0];
    for (int i = n; i < 2 * n; ++i) {
      maxHeap.push(nums[i]);
      prefixSum += nums[i] - maxHeap.top();
      maxHeap.pop();
      ans = min(ans, prefixSum - suffixMax[i - n + 1]);
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
  return solution.minimumDifference(nums);
}
