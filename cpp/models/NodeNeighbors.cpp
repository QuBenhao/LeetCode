//
// Created by BenHao on 2024/7/29.
//

#include "NodeNeighbors.h"
#include <unordered_set>
#include <queue>

Node *JsonArrayToNodeNeighbors(const vector<vector<int>>& arr) {
    if (arr.empty()) {
        return nullptr;
    }
    vector<Node *> nodes = vector<Node *>(arr.size() + 1, nullptr);
    for (size_t i = 1; i <= arr.size(); i++) {
        nodes[i] = new Node(static_cast<int>(i));
    }
    for (size_t i = 0; i < arr.size(); i++) {
        for (size_t j = 0; j < arr[i].size(); j++) {
            nodes[i + 1]->neighbors.emplace_back(nodes[arr[i][j]]);
        }
    }
    return nodes[1];
}

void dfs(Node* cur, vector<vector<int>>& ans, std::unordered_set<int>& visited) {
    int n = static_cast<int>(ans.size());
    if (n < cur->val) {
        for (auto i = n; i < cur->val; i++) {
            ans.emplace_back();
        }
        for (auto neighbor : cur->neighbors) {
            ans.back().emplace_back(neighbor->val);
        }
    } else {
        for (auto neighbor : cur->neighbors) {
            ans[cur->val - 1].emplace_back(neighbor->val);
        }
    }
    for (auto neighbor : cur->neighbors) {
        if (visited.find(neighbor->val) == visited.end()) {
            visited.insert(neighbor->val);
            dfs(neighbor, ans, visited);
        }
    }
}

vector<vector<int>> NodeNeighborsToJsonArray(Node *root) {
    vector<vector<int>> ans;
    if (root == nullptr) {
        return ans;
    }
    std::unordered_set<int> visited;
    visited.insert(root->val);
    dfs(root, ans, visited);
    return ans;
}

void DeleteGraph(Node* root) {
    if (!root) return;
    std::unordered_set<Node*> visited;
    std::queue<Node*> q;
    q.push(root);
    visited.insert(root);
    while (!q.empty()) {
        Node* node = q.front();
        q.pop();
        for (Node* neighbor : node->neighbors) {
            if (neighbor && !visited.count(neighbor)) {
                visited.insert(neighbor);
                q.push(neighbor);
            }
        }
        delete node;
    }
}