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
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
  TreeNode *inorderSuccessor(TreeNode *root, TreeNode *p) {
    if (p->right) {
      p = p->right;
      while (p->left) {
        p = p->left;
      }
      return p;
    }
    TreeNode *successor = nullptr;
    while (root) {
      if (root->val > p->val) {
        successor = root;
        root = root->left;
      } else if (root->val < p->val) {
        root = root->right;
      } else {
        break;
      }
    }
    return successor;
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
  int p_val = json::parse(inputArray.at(1));
  auto nodes = JsonArrayToTreeNodeWithTargets(root_array, {p_val});
  TreeNode *root = nodes[0], *p = nodes[1];
  return TreeNodeToJsonArray(solution.inorderSuccessor(root, p));
}
