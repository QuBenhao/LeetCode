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
        // 存储所有叶节点值的哈希集合
        unordered_set<int> leaves;
        // 存储 (根节点值, 树) 键值对的哈希映射
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

        // 存储中序遍历上一个遍历到的值，便于检查严格单调性
        int prev = 0;

        // 中序遍历，返回值表示是否有严格单调性
        function<bool(TreeNode*)> dfs = [&](TreeNode* tree) {
            if (!tree) {
                return true;
            }

            // 如果遍历到叶节点，并且存在可以合并的树，那么就进行合并
            if (!tree->left && !tree->right && candidates.count(tree->val)) {
                tree->left = candidates[tree->val]->left;
                tree->right = candidates[tree->val]->right;
                // 合并完成后，将树从哈希映射中移除，以便于在遍历结束后判断是否所有树都被遍历过
                candidates.erase(tree->val);
            }

            // 先遍历左子树
            if (!dfs(tree->left)) {
                return false;
            }
            // 再遍历当前节点
            if (tree->val <= prev) {
                return false;
            };
            prev = tree->val;
            // 最后遍历右子树
            return dfs(tree->right);
        };

        for (TreeNode* tree: trees) {
            // 寻找合并完成后的树的根节点
            if (!leaves.count(tree->val)) {
                // 将其从哈希映射中移除
                candidates.erase(tree->val);
                // 从根节点开始进行遍历
                // 如果中序遍历有严格单调性，并且所有树的根节点都被遍历到，说明可以构造二叉搜索树
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
