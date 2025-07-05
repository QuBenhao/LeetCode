//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>

using namespace std;
using json = nlohmann::json;

class FindSumPairs {
  unordered_map<int, int> nums1_map;
  unordered_map<int, int> nums2_map;
  vector<int> nums2;

public:
  FindSumPairs(const vector<int> &nums1, const vector<int> &nums2)
      : nums2(nums2) {
    for (const auto &num : nums1) {
      ++nums1_map[num];
    }
    for (const auto &num : nums2) {
      ++nums2_map[num];
    }
  }

  void add(int index, int val) {
    --nums2_map[nums2[index]];
    nums2[index] += val;
    ++nums2_map[nums2[index]];
  }

  int count(int tot) {
    int count = 0;
    for (const auto &[num1, freq1] : nums1_map) {
      count += nums2_map[tot - num1] * freq1;
    }
    return count;
  }
};

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs* obj = new FindSumPairs(nums1, nums2);
 * obj->add(index,val);
 * int param_2 = obj->count(tot);
 */

json leetcode::qubh::Solve(string input_json_values) {
  vector<string> inputArray;
  size_t pos = input_json_values.find('\n');
  while (pos != string::npos) {
    inputArray.push_back(input_json_values.substr(0, pos));
    input_json_values = input_json_values.substr(pos + 1);
    pos = input_json_values.find('\n');
  }
  inputArray.push_back(input_json_values);

  vector<string> operators = json::parse(inputArray[0]);
  vector<vector<json>> op_values = json::parse(inputArray[1]);
  vector<int> nums2_array = op_values[0][1].get<vector<int>>();
  vector<int> nums1_array = op_values[0][0].get<vector<int>>();
  auto obj0 = make_unique<FindSumPairs>(nums1_array, nums2_array);
  vector<json> ans = {nullptr};
  for (size_t i = 1; i < op_values.size(); ++i) {
    if (operators[i] == "add") {
      obj0->add(op_values[i][0], op_values[i][1]);
      ans.push_back(nullptr);
      continue;
    }
    if (operators[i] == "count") {
      ans.push_back(obj0->count(op_values[i][0]));
      continue;
    }
    ans.push_back(nullptr);
  }
  return ans;
}
