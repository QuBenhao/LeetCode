//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> findKDistantIndices(vector<int> &nums, int key, int k) {
    vector<int> result;
    int n = nums.size();
    int last = -1;
    for (int i = 0; i < n; ++i) {
      if (nums[i] != key)
        continue;
      last = max(last + 1, i - k);
      int nxt = min(n - 1, i + k);
      for (int j = last; j <= nxt; ++j) {
        result.push_back(j);
      }
      last = nxt;
    }
    return result;
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
  int key = json::parse(inputArray.at(1));
  int k = json::parse(inputArray.at(2));
  return solution.findKDistantIndices(nums, key, k);
}
