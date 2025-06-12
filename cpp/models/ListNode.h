//
// Created by BenHao on 2024/5/21.
//

#ifndef LEETCODECPP_LISTNODE_H
#define LEETCODECPP_LISTNODE_H

#include <vector>
#include <tuple>

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

ListNode *IntArrayToListNode(const std::vector<int> &arr);

std::vector<int> ListNodeToIntArray(ListNode *head);

ListNode *IntArrayToListNodeCycle(std::vector<int> &arr, int pos);

std::tuple<ListNode *, ListNode *>
IntArrayToIntersectionListNode(int iv, std::vector<int> &arr1, std::vector<int> &arr2, int idx_a, int idx_b);

#endif //LEETCODECPP_LISTNODE_H
