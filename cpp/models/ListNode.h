//
// Created by 曲本豪 on 2024/5/21.
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

ListNode *IntArrayToListNode(std::vector<int> &arr);

std::vector<int> &ListNodeToIntArray(ListNode *head);

std::tuple<ListNode *, ListNode *>
IntArrayToIntersectionListNode(std::vector<int> &arr1, std::vector<int> &arr2, int iv, int idxA, int idxB);

#endif //LEETCODECPP_LISTNODE_H
