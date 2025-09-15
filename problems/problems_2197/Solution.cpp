//go:build ignore
#include "cpp/common/Solution.h"
#include <numeric>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> replaceNonCoprimes(const vector<int> &nums) {
    vector<int> st;
    for (auto num : nums) {
      while (!st.empty()) {
        int g = std::gcd(num, st.back());
        if (g == 1) {
          break;
        }
        num = st.back() / g * num;
        st.pop_back();
      }
      st.push_back(num);
    }
    return st;
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
  return solution.replaceNonCoprimes(nums);
}
