//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size(), steps = 0;
        for (int left = 0, right = 0; right < n-1; steps++) { // right: 当前能走到的最远坐标
            int tmp = right;
            for (int c = left; c <= tmp; c++) {
                right = max(right, c+nums[c]);
            }
            left = tmp + 1; // 跳跃一次, 上次在[left, tmp], 下次在[tmp+1, right]
        }
        return steps;
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
  return solution.jump(nums);
}
