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
  int sumRootToLeaf(TreeNode *root) {
    if (root == nullptr) {
      return 0;
    }
    auto dfs = [](this auto &&dfs, TreeNode *node, int cur) -> int {
      cur <<= 1;
      cur += node->val;
      if (node->left == nullptr && node->right == nullptr) {
        return cur;
      }
      int ans = 0;
      if (node->left != nullptr) {
        ans += dfs(node->left, cur);
      }
      if (node->right != nullptr) {
        ans += dfs(node->right, cur);
      }
      return ans;
    };

    return dfs(root, 0);
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
  json final_ans = solution.sumRootToLeaf(root);
  delete root;
  return final_ans;
}
