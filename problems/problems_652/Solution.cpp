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
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
  vector<TreeNode *> findDuplicateSubtrees(TreeNode *root) {
    unordered_map<string, TreeNode *> cache;
    unordered_map<string, TreeNode *> res_cache;
    auto dfs = [&cache, &res_cache](this auto &&dfs, TreeNode *node) -> string {
      if (!node)
        return " ";
      string left = dfs(node->left);
      string right = dfs(node->right);
      string curr = to_string(node->val) + "," + left + "," + right;
      if (cache.count(curr) && !res_cache.count(curr)) {
        res_cache[curr] = node;
      }
      cache[curr] = node;
      return curr;
    };
    dfs(root);
    vector<TreeNode *> res;
    for (const auto &[key, value] : res_cache) {
      res.push_back(value);
    }
    return res;
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
  vector<TreeNode *> res_ptr_list = solution.findDuplicateSubtrees(root);
  json final_ans = TreeNodeArrayToJsonArray(res_ptr_list);
  delete root;
  // for (auto ptr : res_ptr_list) {
  //   delete ptr;
  // }
  // res_ptr_list.clear();  // Clear the vector to prevent memory leak
  return final_ans;
}
