//
// Created by BenHao on 2024/7/28.
//

#ifndef LEETCODE_TREENODENEXT_H
#define LEETCODE_TREENODENEXT_H

#include <nlohmann/json.hpp>

using json = nlohmann::json;

// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(nullptr), right(nullptr), next(nullptr) {}

    explicit Node(int _val) : val(_val), left(nullptr), right(nullptr), next(nullptr) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};

Node *JsonArrayToTreeNodeNext(json arr);
json TreeNodeNextToJsonArray(Node *root);


#endif //LEETCODE_TREENODENEXT_H
