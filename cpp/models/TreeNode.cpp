#include "TreeNode.h"
#include <queue>


TreeNode *JsonArrayToTreeNode(json arr) {
    if (arr.empty()) {
        return nullptr;
    }
    auto root = new TreeNode(arr[0]);
    int isLeft = true;
    std::queue<TreeNode *> q;
    auto curr_node = root;
    for (size_t i = 1; i < arr.size(); i++) {
        json num = arr[i];
        if (isLeft == 1) {
            if (num != nullptr) {
                curr_node->left = new TreeNode(int(num));
                q.push(curr_node->left);
            }
        } else {
            if (num != nullptr) {
                curr_node->right = new TreeNode(int(num));
                q.push(curr_node->right);
            }
            curr_node = q.front();
            q.pop();
        }
        isLeft ^= 1;
    }
    return root;
}

std::vector<TreeNode*> JsonArrayToTreeNodeArray(json arr) {
    if (arr.empty()) {
        return {};
    }
    auto ans = std::vector<TreeNode*>(arr.size(), nullptr);
    for (auto i = 0; i < arr.size(); i++) {
        ans[i] = JsonArrayToTreeNode(arr[i]);
    }
    return ans;
}

json TreeNodeToJsonArray(TreeNode *root) {
    json ans = json::array();
    std::queue<TreeNode *> q;
    q.push(root);
    while (!q.empty()) {
        TreeNode *node = q.front();
        q.pop();
        if (node != nullptr) {
            ans.push_back(node->val);
            q.push(node->left);
            q.push(node->right);
        } else {
            ans.push_back(nullptr);
        }
    }
    while (!ans.empty() && ans.back() == nullptr) {
        ans.erase(ans.end() - 1);
    }
    return ans;
}