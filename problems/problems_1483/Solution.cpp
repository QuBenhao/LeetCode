//go:build ignore
#include "cpp/common/Solution.h"

#include <vector>

using namespace std;
using json = nlohmann::json;

class TreeAncestor {
  vector<vector<int>> pa;

public:
  TreeAncestor(int n, vector<int> &parent) {
    int m;
    for (m = 1; (1 << m) < n; ++m) {
    }
    pa = vector<vector<int>>(n, vector<int>(m + 1, -1));
    for (int i = 0; i < n; ++i) {
      pa[i][0] = parent[i];
    }
    for (int j = 1; j <= m; ++j) {
      for (int i = 0; i < n; ++i) {
        if (pa[i][j - 1] != -1) {
          pa[i][j] = pa[pa[i][j - 1]][j - 1];
        }
      }
    }
  }

  int getKthAncestor(int node, int k) {
    for (; k > 0 && node != -1; k &= k - 1) {
      node = pa[node][__builtin_ctz(k)];
    }
    return node;
  }
};

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * TreeAncestor* obj = new TreeAncestor(n, parent);
 * int param_1 = obj->getKthAncestor(node,k);
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
  vector<int> parent_array = op_values[0][1].get<vector<int>>();
  auto obj0 = make_unique<TreeAncestor>(op_values[0][0], parent_array);
  vector<json> ans = {nullptr};
  for (size_t i = 1; i < op_values.size(); ++i) {
    if (operators[i] == "getKthAncestor") {
      ans.push_back(obj0->getKthAncestor(op_values[i][0], op_values[i][1]));
      continue;
    }
    ans.push_back(nullptr);
  }
  return ans;
}
