//go:build ignore
#include "cpp/common/Solution.h"
#include "cpp/models/TreeNode.h"

using namespace std;
using json = nlohmann::json;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
public:
  int maxPathSum(TreeNode *root) {
    int ans = -0x3f3f3f3f;
    function<int(TreeNode *)> dfs = [&](TreeNode *node) {
      if (!node)
        return 0;
      int left = dfs(node->left);
      int right = dfs(node->right);
      ans = max(ans, node->val + left + right);
      return max(0, node->val + max(left, right));
    };
    dfs(root);
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
  json root_array = json::parse(inputArray.at(0));
  TreeNode *root = JsonArrayToTreeNode(root_array);
  return solution.maxPathSum(root);
}
