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
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        if (original == nullptr || original == target) {
            return cloned;
        }
        TreeNode *left = getTargetCopy(original->left, cloned->left, target);
        if (left != nullptr) {
            return left;
        }
        return getTargetCopy(original->right, cloned->right, target);
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
	json original_array = json::parse(inputArray.at(0));
	int target_val = json::parse(inputArray.at(1));
	auto nodes = JsonArrayToTreeNodeWithTargets(original_array, {target_val});
	TreeNode *original = nodes[0];
	TreeNode *target = nodes[1];
	TreeNode *cloned = JsonArrayToTreeNode(original_array);
	TreeNode *res_ptr = solution.getTargetCopy(original, cloned, target);
	json final_ans = TreeNodeToJsonArray(res_ptr);
	delete original;
	delete cloned;
	// delete res_ptr;
	return final_ans;
}
