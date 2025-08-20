//
// Created by BenHao on 2024/5/21.
//

#ifndef LEETCODECPP_LISTNODE_H
#define LEETCODECPP_LISTNODE_H

#include <tuple>
#include <vector>

struct ListNode {
  int val;
  ListNode *next;

  ListNode() : val(0), next(nullptr) {}

  ListNode(int x) : val(x), next(nullptr) {}

  ListNode(int x, ListNode *next) : val(x), next(next) {}

  ~ListNode() { delete next; }
};

ListNode *IntArrayToListNode(const std::vector<int> &arr);

std::vector<int> ListNodeToIntArray(ListNode *head);

std::vector<std::vector<int>>
ListNodesToIntArrays(const std::vector<ListNode *> &heads);

ListNode *IntArrayToListNodeCycle(const std::vector<int> &arr, int pos);

std::tuple<ListNode *, ListNode *>
IntArrayToIntersectionListNode(int iv, const std::vector<int> &arr1,
                               const std::vector<int> &arr2, int idx_a,
                               int idx_b);

#endif  // LEETCODECPP_LISTNODE_H
