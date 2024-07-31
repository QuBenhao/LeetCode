//
// Created by BenHao on 2024/7/29.
//

#ifndef LEETCODE_NODERANDOM_H
#define LEETCODE_NODERANDOM_H

#include "nlohmann/json.hpp"
#include <vector>

using std::vector;
using nlohmann::json;

// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    explicit Node(int _val) {
        val = _val;
        next = nullptr;
        random = nullptr;
    }
};

Node* JsonArrayToNodeRandom(json arr);
json NodeRandomToJsonArray(Node* head);

#endif //LEETCODE_NODERANDOM_H
