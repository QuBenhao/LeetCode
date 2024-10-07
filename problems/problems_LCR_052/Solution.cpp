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
private:
  void inorder(TreeNode *root, TreeNode *&prev) {
    if (root == nullptr) {
      return;
    }
    inorder(root->left, prev);
    prev->right = root;
    root->left = nullptr;
    prev = root;
    inorder(root->right, prev);
  }

public:
  TreeNode *increasingBST(TreeNode *root) {
    TreeNode *dummy = new TreeNode(-1);
    TreeNode *prev = dummy;
    inorder(root, prev);
    return dummy->right;
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
  return TreeNodeToJsonArray(solution.increasingBST(root));
}
