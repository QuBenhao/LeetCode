//
// Created by 曲本豪 on 2024/5/21.
//

#ifndef LEETCODECPP_LISTNODE_H
#define LEETCODECPP_LISTNODE_H

#include <vector>

struct ListNode {
    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {}

    ListNode(int x) : val(x), next(nullptr) {}

    ListNode(int x, ListNode *next) : val(x), next(next) {}

    ~ListNode() {
        delete next;
    }
};

ListNode *IntArrayToListNode(std::vector<int> &arr);
std::vector<int> &ListNodeToIntArray(ListNode *head);

#endif //LEETCODECPP_LISTNODE_H
