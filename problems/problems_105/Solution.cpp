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
  TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
    if (preorder.empty()) {
      return nullptr;
    }
    int root_val = preorder[0];
    TreeNode *root = new TreeNode(root_val);
    int root_index = 0;
    for (int i = 0; i < inorder.size(); i++) {
      if (inorder[i] == root_val) {
        root_index = i;
        break;
      }
    }
    vector<int> left_preorder(preorder.begin() + 1,
                              preorder.begin() + 1 + root_index);
    vector<int> right_preorder(preorder.begin() + 1 + root_index,
                               preorder.end());
    vector<int> left_inorder(inorder.begin(), inorder.begin() + root_index);
    vector<int> right_inorder(inorder.begin() + root_index + 1, inorder.end());
    root->left = buildTree(left_preorder, left_inorder);
    root->right = buildTree(right_preorder, right_inorder);
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
  vector<int> preorder = json::parse(inputArray.at(0));
  vector<int> inorder = json::parse(inputArray.at(1));
  return TreeNodeToJsonArray(solution.buildTree(preorder, inorder));
}
