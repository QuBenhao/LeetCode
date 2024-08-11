//go:build ignore
#include "cpp/common/Solution.h"
#include "cpp/models/TreeNode.h"
#include <vector>

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
	void inorder(TreeNode* root, vector<int>& ans) {
		if (root == nullptr) {
			return;
		}
		inorder(root->left, ans);
		ans.push_back(root->val);
		inorder(root->right, ans);
	}
public:
    int kthSmallest(TreeNode* root, int k) {
		vector<int> ans;
		inorder(root, ans);
		return ans[k - 1];
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
	int k = json::parse(inputArray.at(1));
	return solution.kthSmallest(root, k);
}
