//go:build ignore
#include "cpp/common/Solution.h"
#include "cpp/models/TreeNode.h"
#include <deque>

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
    vector<int> rightSideView(TreeNode* root) {
		vector<int> res;
		if (root == nullptr) {
			return res;
		}
		deque<TreeNode*> q;
		q.push_back(root);
		while (!q.empty()) {
			size_t n = q.size();
			TreeNode* node;
			for (size_t i = 0; i < n; i++) {
				node = q.front();
				q.pop_front();
				if (node->left != nullptr) {
					q.push_back(node->left);
				}
				if (node->right != nullptr) {
					q.push_back(node->right);
				}
			}
			res.push_back(node->val);
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
	return solution.rightSideView(root);
}
