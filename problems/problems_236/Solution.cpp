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
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == nullptr || root == p || root == q) {
            return root;
        }
        TreeNode *left = lowestCommonAncestor(root->left, p, q);
        TreeNode *right = lowestCommonAncestor(root->right, p, q);
        if (left != nullptr && right != nullptr) {
            return root;
        }
        return left != nullptr ? left : right;
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
	int p_val = json::parse(inputArray.at(1));
	int q_val = json::parse(inputArray.at(2));
	auto nodes = JsonArrayToTreeNodeWithTargets(root_array, {p_val, q_val});
	TreeNode *root = nodes[0], *p = nodes[1], *q = nodes[2];
	return TreeNodeToJsonArray(solution.lowestCommonAncestor(root, p, q));
}
