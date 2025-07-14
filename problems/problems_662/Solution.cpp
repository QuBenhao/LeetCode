//go:build ignore
#include "cpp/common/Solution.h"
#include "cpp/models/TreeNode.h"

#include <queue>

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
  int widthOfBinaryTree(TreeNode *root) {
    if (root == nullptr)
      return 0;
    int ans = 0;
    queue<pair<uint32_t, TreeNode *>> q;
    q.emplace(0, root);
    while (!q.empty()) {
      int size = q.size();
      ans = max(ans, static_cast<int>(q.back().first - q.front().first + 1));
      for (int i = 0; i < size; ++i) {
        auto [index, node] = q.front();
        q.pop();
        if (node->left) {
          q.emplace(2 * index, node->left);
        }
        if (node->right) {
          q.emplace(2 * index + 1, node->right);
        }
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
  json root_array = json::parse(inputArray.at(0));
  TreeNode *root = JsonArrayToTreeNode(root_array);
  json final_ans = solution.widthOfBinaryTree(root);
  delete root;
  return final_ans;
}
