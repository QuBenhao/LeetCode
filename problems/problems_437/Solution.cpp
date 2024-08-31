// go:build ignore
#include <unordered_map>
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
  int pathSum(TreeNode *root, int targetSum) {
    function<int(TreeNode *, unordered_map<uint64_t, int> &, uint64_t)> dfs =
        [&](TreeNode *node, unordered_map<uint64_t, int> &counter,
            uint64_t cur_sum) -> int {
      if (!node) {
        return 0;
      }
      cur_sum += node->val;
      int res = counter[cur_sum - targetSum];
      counter[cur_sum]++;
      res += dfs(node->left, counter, cur_sum);
      res += dfs(node->right, counter, cur_sum);
      counter[cur_sum]--;
      return res;
    };
    unordered_map<uint64_t, int> counter;
    counter[0] = 1;
    return dfs(root, counter, 0);
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
  int targetSum = json::parse(inputArray.at(1));
  return solution.pathSum(root, targetSum);
}
