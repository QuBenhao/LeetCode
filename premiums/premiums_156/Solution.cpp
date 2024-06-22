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
public:
    TreeNode *upsideDownBinaryTree(TreeNode *root) {
        TreeNode *node = nullptr, *left = root, *right = nullptr;
        while (left != nullptr) {
            TreeNode *new_left = left->left, *new_right = left->right;
            left->left = right;
            left->right = node;
            node = left;
            left = new_left;
            right = new_right;
        }
        return node;
    }
};

json leetcode::qubh::Solve(string input) {
    vector<string> inputArray;
    size_t pos = input.find('\n');
    while (pos != string::npos) {
        inputArray.push_back(input.substr(0, pos));
        input = input.substr(pos + 1);
        pos = input.find('\n');
    }
    inputArray.push_back(input);

    Solution solution;
    json root_array = json::parse(inputArray.at(0));
    TreeNode *root = JsonArrayToTreeNode(root_array);
    return TreeNodeToJsonArray(solution.upsideDownBinaryTree(root));
}
