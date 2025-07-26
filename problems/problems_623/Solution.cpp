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
  TreeNode *addOneRow(TreeNode *root, int val, int depth) {
    if (depth == 1) {
      return new TreeNode(val, root, nullptr);
    }

    auto dfs = [&](this auto &&dfs, TreeNode *node, int cur_d) -> void {
      if (!node)
        return;
      if (cur_d == depth - 1) {
        node->left = new TreeNode(val, node->left, nullptr);
        node->right = new TreeNode(val, nullptr, node->right);
      } else {
        dfs(node->left, cur_d + 1);
        dfs(node->right, cur_d + 1);
      }
    };
    dfs(root, 1);
    return root;
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
  int val = json::parse(inputArray.at(1));
  int depth = json::parse(inputArray.at(2));
  TreeNode *res_ptr = solution.addOneRow(root, val, depth);
  json final_ans = TreeNodeToJsonArray(res_ptr);
  // delete root;
  delete res_ptr;
  return final_ans;
}
