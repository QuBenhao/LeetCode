//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>

using namespace std;
using json = nlohmann::json;

class Solution {
  vector<int> prefix;

public:
  Solution(vector<int> &w) {
    int n = w.size();
    prefix = vector<int>(n + 1);
    for (int i = 0; i < n; i++) {
      prefix[i + 1] = prefix[i] + w[i];
    }
  }

  int pickIndex() {
    int v = rand() % prefix.back() + 1;
    return lower_bound(prefix.begin(), prefix.end(), v) - prefix.begin() - 1;
  }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
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
  vector<int> w_array = op_values[0][0].get<vector<int>>();
  auto obj0 = make_shared<Solution>(w_array);
  vector<json> ans = {nullptr};
  for (size_t i = 1; i < op_values.size(); i++) {
    if (operators[i] == "pickIndex") {
      ans.push_back(obj0->pickIndex());
      continue;
    }
    ans.push_back(nullptr);
  }
  return ans;
}
