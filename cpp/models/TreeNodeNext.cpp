//
// Created by BenHao on 2024/7/28.
//

#include "TreeNodeNext.h"
#include <queue>

using std::queue;

Node *JsonArrayToTreeNodeNext(json arr) {
 if (arr.empty()) {
        return nullptr;
    }
    auto root = new Node(arr[0]);
    int isLeft = true;
    queue<Node *> q;
    auto curr_node = root;
    for (size_t i = 1; i < arr.size(); i++) {
        json num = arr[i];
        if (isLeft == 1) {
            if (num != nullptr) {
                curr_node->left = new Node(static_cast<int>(num));
                q.push(curr_node->left);
            }
        } else {
            if (num != nullptr) {
                curr_node->right = new Node(static_cast<int>(num));
                q.push(curr_node->right);
            }
            curr_node = q.front();
            q.pop();
        }
        isLeft ^= 1;
    }
    return root;
}

json TreeNodeNextToJsonArray(Node *root) {
    json ans = json::array();
    if (root == nullptr) {
        return ans;
    }
    Node* head = root;
    while (head != nullptr) {
        Node* next_head = nullptr, *cur = head;
        while (cur != nullptr) {
            if (next_head == nullptr) {
                next_head = cur->left != nullptr ? cur->left : cur->right;
            }
            ans.push_back(cur->val);
            cur = cur->next;
        }
        ans.push_back(nullptr);
        head = next_head;
    }
    return ans;
}