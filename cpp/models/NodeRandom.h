//
// Created by BenHao on 2024/7/29.
//

#ifndef LEETCODE_NODERANDOM_H
#define LEETCODE_NODERANDOM_H

#include "nlohmann/json.hpp"
#include <vector>
#include <variant>

using std::vector;
using std::variant;

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

Node* JsonArrayToNodeRandom(vector<vector<variant<int, nullptr_t>>> arr);

#endif //LEETCODE_NODERANDOM_H
