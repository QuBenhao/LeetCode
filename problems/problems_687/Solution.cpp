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
  int longestUnivaluePath(TreeNode *root) {
    int ans = 0;

    auto dfs = [&ans](this auto &&dfs, TreeNode *node) -> int {
      if (node == nullptr) {
        return 0;
      }
      int cur_ans = 0, cur = 0, left = dfs(node->left),
          right = dfs(node->right);
      if (node->left != nullptr && node->left->val == node->val) {
        cur_ans = left + 1;
        cur += left + 1;
      }
      if (node->right != nullptr && node->right->val == node->val) {
        cur_ans = max(cur_ans, right + 1);
        cur += right + 1;
      }
      ans = max(ans, cur);
      return cur_ans;
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
  json final_ans = solution.longestUnivaluePath(root);
  delete root;
  return final_ans;
}
