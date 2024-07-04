//
// Created by 曲本豪 on 2024/5/21.
//

#include "ListNode.h"

ListNode *IntArrayToListNode(std::vector<int> &arr) {
    auto dummy = new ListNode(), p = dummy;
    for (auto val : arr) {
        p->next = new ListNode(val);
        p = p->next;
    }
    return dummy->next;
}

std::vector<int> &ListNodeToIntArray(ListNode *head) {
    auto *arr = new std::vector<int>();
    while (head != nullptr) {
        arr->push_back(head->val);
        head = head->next;
    }
    return *arr;
}
