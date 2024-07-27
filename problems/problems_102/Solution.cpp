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
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        if (root == nullptr) return ans;
        deque<TreeNode*> q = {root};
        while (!q.empty()) {
            vector<int> cur;
            for (int i = q.size(); i > 0; i--) {
                TreeNode* node = q.front();
                q.pop_front();
                cur.emplace_back(node->val);
                if (node->left) q.emplace_back(node->left);
                if (node->right) q.emplace_back(node->right);
            }
            ans.emplace_back(cur);
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
	return solution.levelOrder(root);
}
