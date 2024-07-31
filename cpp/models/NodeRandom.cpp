//
// Created by BenHao on 2024/7/29.
//

#include "NodeRandom.h"
#include <unordered_map>

Node* JsonArrayToNodeRandom(json arr) {
    if (arr.empty()) {
        return nullptr;
    }
    vector<Node*> nodes = vector<Node*>(arr.size());
    for (int i = 0; i < static_cast<int>(arr.size()); i++) {
        nodes[i] = new Node(0);
    }
    for (int i = 0; i < static_cast<int>(arr.size()); i++) {
        auto node = nodes[i];
        node->val = arr[i][0];
        if (i < static_cast<int>(arr.size()) - 1) {
            node->next = nodes[i + 1];
        }
        if (!arr[i][1].is_null()) {
            node->random = nodes[arr[i][1]];
        }
    }
    return nodes[0];
}

json NodeRandomToJsonArray(Node* head) {
    json arr = json::array();
    std::unordered_map<Node*, int> nodeMap;
    int index = 0;
    Node* node = head;
    while (node != nullptr) {
        nodeMap[node] = index;
        node = node->next;
        index++;
    }
    node = head;
    while (node != nullptr) {
        json item = json::array();
        item.push_back(node->val);
        if (node->random != nullptr) {
            item.push_back(nodeMap[node->random]);
        } else {
            item.push_back(nullptr);
        }
        arr.push_back(item);
        node = node->next;
    }
    return arr;
}