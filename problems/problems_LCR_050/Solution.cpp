//go:build ignore
#include "cpp/common/Solution.h"
#include "cpp/models/TreeNode.h"
#include <unordered_map>

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
  int pathSum(TreeNode *root, int targetSum) {
    const function<int(TreeNode *, unordered_map<int64_t, int> &, int64_t)> dfs =
        [&](TreeNode *node, unordered_map<int64_t, int> &prefixSum,
            int64_t currentSum) -> int {
      if (node == nullptr) {
        return 0;
      }
      int result = 0;
      currentSum += node->val;
      result += prefixSum[currentSum - targetSum];
      prefixSum[currentSum]++;
      result += dfs(node->left, prefixSum, currentSum);
      result += dfs(node->right, prefixSum, currentSum);
      prefixSum[currentSum]--;
      return result;
    };
    unordered_map<int64_t, int> prefixSum;
    prefixSum[0] = 1;
    return dfs(root, prefixSum, 0);
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
