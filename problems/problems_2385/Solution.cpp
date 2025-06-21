//go:build ignore
#include <utility>

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
  int amountOfTime(TreeNode *root, int start) {
    int ans = 0;
    auto dfs = [&ans, start](this auto &&dfs, const TreeNode * const node) {
      if (!node)
        return make_pair(0, false);
      if (node->val == start) {
        auto left = dfs(node->left);
        auto right = dfs(node->right);
        ans = max(left.first, right.first);
        return make_pair(0, true);
      }
      auto [l, foundLeft] = dfs(node->left);
      auto [r, foundRight] = dfs(node->right);
      int d = 1;
      if (foundLeft || foundRight) {
        ans = max(ans, l + r + 1);
        if (foundLeft) {
          d = l + 1;
        } else {
          d = r + 1;
        }
      } else {
        d = max(l, r) + 1;
      }
      return make_pair(d, foundLeft || foundRight);
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
  int start = json::parse(inputArray.at(1));
  json final_ans = solution.amountOfTime(root, start);
  delete root;
  return final_ans;
}
