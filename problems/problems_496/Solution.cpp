//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> nextGreaterElement(const vector<int> &nums1,
                                 const vector<int> &nums2) {
    int n = nums1.size();
    unordered_map<int, int> idx_map(n);
    vector<int> result(n, -1);
    for (int i = 0; i < n; ++i) {
      idx_map[nums1[i]] = i;
    }
    stack<int> stack;
    for (auto &num : nums2) {
      while (!stack.empty() && stack.top() < num) {
        if (idx_map.count(stack.top())) {
          result[idx_map[stack.top()]] = num;
        }
        stack.pop();
      }
      stack.push(num);
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
  vector<int> nums1 = json::parse(inputArray.at(0));
  vector<int> nums2 = json::parse(inputArray.at(1));
  return solution.nextGreaterElement(nums1, nums2);
}
