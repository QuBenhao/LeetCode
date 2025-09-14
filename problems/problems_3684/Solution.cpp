//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> maxKDistinct(const vector<int> &nums, int k) {
    set<int> st(nums.begin(), nums.end());
    vector<int> ans;
    for (auto it = st.rbegin(); it != st.rend() && ans.size() < k;
         it = next(it)) {
      ans.emplace_back(*it);
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
  return solution.maxKDistinct(nums, k);
}
