//go:build ignore
#include "cpp/common/Solution.h"

#include <stack>
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int numSubmat(vector<vector<int>> &mat) {
    int n = mat[0].size();
    int ans = 0;
    vector<int> heights(n, 0);
    for (auto &row : mat) {
      vector<int> st;
      vector<int> prev(n, 0);
      int pre_sum = 0;
      for (int j = 0; j < n; ++j) {
        if (row[j] == 0) {
          heights[j] = 0;
        } else {
          heights[j]++;
        }
        while (!st.empty() && heights[st.back()] >= heights[j]) {
          pre_sum -= prev[st.back()];
          st.pop_back();
        }
        prev[j] = heights[j] * (st.empty() ? j + 1 : j - st.back());
        pre_sum += prev[j];
        st.push_back(j);
        ans += pre_sum;
      }
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
  vector<vector<int>> mat = json::parse(inputArray.at(0));
  return solution.numSubmat(mat);
}
