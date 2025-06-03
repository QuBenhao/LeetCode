//go:build ignore
#include "cpp/common/Solution.h"

#include <algorithm>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        int i;
        for (i = n - 2; i >= 0; i--) {
            if (nums[i] < nums[i+1]) {
                break;
            }
        }
        // for (int l = i + 1, r = n - 1; l < r; l++, r--) {
        //     swap(nums[l], nums[r]);
        // }
        reverse(nums.begin()+i+1, nums.end());
        if (i >= 0) {
            auto it = upper_bound(nums.begin() + i + 1, nums.end(), nums[i]);
            iter_swap(nums.begin()+i, it);
        }
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
  solution.nextPermutation(nums);
  return nums;
}
