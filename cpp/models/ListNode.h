//
// Created by 曲本豪 on 2024/5/21.
//

#ifndef LEETCODECPP_LISTNODE_H
#define LEETCODECPP_LISTNODE_H

struct ListNode {
    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {}

    ListNode(int x) : val(x), next(nullptr) {}

    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

#endif //LEETCODECPP_LISTNODE_H
