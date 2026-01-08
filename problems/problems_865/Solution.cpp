//go:build ignore
#include "cpp/common/Solution.h"
#include "cpp/models/TreeNode.h"
#include <utility>

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
  TreeNode *subtreeWithAllDeepest(TreeNode *root) {
    auto dfs = [](this auto &&dfs, TreeNode *node) -> std::pair<TreeNode *, int> {
      if (node == nullptr) {
        return {node, 0};
      }
      auto [left, leftV] = dfs(node->left);
      auto [right, rightV] = dfs(node->right);
      if (leftV == rightV) {
        return {node, leftV + 1};
      } else if (leftV > rightV) {
        return {left, leftV + 1};
      } else {
        return {right, rightV + 1};
      }
    };
    auto [node, _] = dfs(root);
    return node;
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
  TreeNode *res_ptr = solution.subtreeWithAllDeepest(root);
  json final_ans = TreeNodeToJsonArray(res_ptr);
  // delete root;
  delete res_ptr;
  return final_ans;
}
