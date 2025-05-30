//go:build ignore
#include "cpp/common/Solution.h"
#include "cpp/models/TreeNode.h"

#include <stack>

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
    bool findTarget(TreeNode* root, int k) {
        stack<TreeNode*> left, right; // 左右栈分别存放中序遍历和逆中序遍历的节点
        auto expend = [&](TreeNode* nd, bool is_left) { // 展开一个节点的子树, 栈的方式遍历树
            nd = is_left ? nd->right : nd->left;
            while(nd != nullptr) {
                if (is_left) {
                    left.push(nd);
                } else {
                    right.push(nd);
                }
                nd = is_left ? nd->left : nd->right;
            }
        };

        TreeNode* node = root;
        while (node != nullptr) {
            left.push(node);
            node = node->left;
        }
        node = root;
        while (node != nullptr) {
            right.push(node);
            node = node->right;
        }
        TreeNode* left_ptr = left.top(), *right_ptr = right.top(); // 左指针和右指针
        while (left_ptr->val < right_ptr->val) { // 左指针和右指针没有相遇
            int s = left_ptr->val + right_ptr->val;
            if (s == k) { // 找到目标值
                return true;
            } else if (s > k) { // 和大于目标值, 右指针左移
                right.pop();
                expend(right_ptr, false);
                right_ptr = right.top();
            } else { // 和小于目标值, 左指针右移
                left.pop();
                expend(left_ptr, true);
                left_ptr = left.top();
            }
        }
        return false;
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
	return solution.findTarget(root, k);
}
