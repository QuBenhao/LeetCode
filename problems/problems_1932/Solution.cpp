//go:build ignore
#include "cpp/common/Solution.h"
#include "cpp/models/TreeNode.h"
#include <unordered_set>
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
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* canMerge(vector<TreeNode*>& trees) {
        // Hash set of all leaf values
        unordered_set<int> leaves;
        // Hash map from root values to trees
        unordered_map<int, TreeNode*> candidates;
        for (TreeNode* tree: trees) {
            if (tree->left) {
                leaves.insert(tree->left->val);
            }
            if (tree->right) {
                leaves.insert(tree->right->val);
            }
            candidates[tree->val] = tree;
        }

        // Previous inorder value, used to check strict increase
        int prev = 0;

        // Inorder traversal; return whether values are strictly increasing
        function<bool(TreeNode*)> dfs = [&](TreeNode* tree) {
            if (!tree) {
                return true;
            }

            // Merge when a leaf has a matching tree available
            if (!tree->left && !tree->right && candidates.count(tree->val)) {
                tree->left = candidates[tree->val]->left;
                tree->right = candidates[tree->val]->right;
                // Remove the merged tree from the map so we can later check that every tree was visited
                candidates.erase(tree->val);
            }

            // Traverse the left subtree first
            if (!dfs(tree->left)) {
                return false;
            }
            // Then visit the current node
            if (tree->val <= prev) {
                return false;
            };
            prev = tree->val;
            // Finally traverse the right subtree
            return dfs(tree->right);
        };

        for (TreeNode* tree: trees) {
            // Find the root of the merged tree
            if (!leaves.count(tree->val)) {
                // Remove it from the hash map
                candidates.erase(tree->val);
                // Traverse from the root
                // A strictly increasing inorder traversal that visits every tree root forms a valid BST
                return (dfs(tree) && candidates.empty()) ? tree : nullptr;
            }
        }
        return nullptr;
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
	json trees_array = json::parse(inputArray.at(0));
	vector<TreeNode*> trees = JsonArrayToTreeNodeArray(trees_array);
	return TreeNodeToJsonArray(solution.canMerge(trees));
}
