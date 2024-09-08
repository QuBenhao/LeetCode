//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> sortedSquares(vector<int> &nums) {
    int n = static_cast<int>(nums.size());
    vector<int> result(n);
    for (int left = 0, right = n - 1, index = n - 1; left <= right; index--) {
      if (nums[left] * nums[left] > nums[right] * nums[right]) {
        result[index] = nums[left] * nums[left];
        left++;
      } else {
        result[index] = nums[right] * nums[right];
        right--;
      }
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
  return solution.sortedSquares(nums);
}
