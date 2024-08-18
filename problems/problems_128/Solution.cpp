//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_map>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int longestConsecutive(vector<int> &nums) {
    unordered_map<int, int> map;
    int res = 0;
    for (auto num : nums) {
      if (map.find(num) == map.end()) {
        int left = map.find(num - 1) != map.end() ? map[num - 1] : 0;
        int right = map.find(num + 1) != map.end() ? map[num + 1] : 0;
        int length = left + right + 1;
		res = max(res, length);
        map[num] = length;
        map[num - left] = length;
        map[num + right] = length;
      }
    }
    return res;
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
  return solution.longestConsecutive(nums);
}
