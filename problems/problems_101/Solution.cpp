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
private:
    bool dfs(TreeNode* left, TreeNode* root) {
        if (left == nullptr && root == nullptr) {
            return true;
        } else if (left == nullptr || root == nullptr) {
            return false;
        }
        return left->val == root->val && dfs(left->left, root->right) && dfs(left->right, root->left);
    }
public:
    bool isSymmetric(TreeNode* root) {
        return root == nullptr || dfs(root->left, root->right);
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
	return solution.isSymmetric(root);
}
