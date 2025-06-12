//
// Created by BenHao on 2024/7/29.
//

#ifndef LEETCODE_NODENEIGHBORS_H
#define LEETCODE_NODENEIGHBORS_H

#include <utility>
#include <vector>
#include <nlohmann/json.hpp>

using json = nlohmann::json;
using std::vector;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node *> neighbors;

    Node() {
        val = 0;
        neighbors = vector<Node *>();
    }

    explicit Node(int _val) {
        val = _val;
        neighbors = vector<Node *>();
    }

    Node(int _val, vector<Node *> _neighbors) {
        val = _val;
        neighbors = std::move(_neighbors);
    }
};

Node *JsonArrayToNodeNeighbors(const vector<vector<int>>& arr);
vector<vector<int>> NodeNeighborsToJsonArray(Node *root);
void DeleteGraph(Node* root);

#endif //LEETCODE_NODENEIGHBORS_H
