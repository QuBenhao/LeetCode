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
	bool dfs(TreeNode* root, TreeNode* subRoot, bool must_match) {
		if (root == nullptr || subRoot == nullptr) {
			return root == subRoot;
		}
		if (root->val == subRoot->val && dfs(root->left, subRoot->left, true) && dfs(root->right, subRoot->right, true)) {
			return true;
		}
		if (must_match) {
			return false;
		}
		return dfs(root->left, subRoot, false) || dfs(root->right, subRoot, false);
	}
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
		return dfs(root, subRoot, false);
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
	json subRoot_array = json::parse(inputArray.at(1));
	TreeNode *subRoot = JsonArrayToTreeNode(subRoot_array);
	return solution.isSubtree(root, subRoot);
}
