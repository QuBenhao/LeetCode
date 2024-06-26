//
// Created by 曲本豪 on 2024/5/21.
//

#include "ListNode.h"

ListNode *IntArrayToListNode(std::vector<int> &arr) {
    ListNode *dummy = new ListNode();
    ListNode *p = dummy;
    for (size_t i = 0; i < arr.size(); i++) {
        p->next = new ListNode(arr[i]);
        p = p->next;
    }
    return dummy->next;
}

std::vector<int> &ListNodeToIntArray(ListNode *head) {
    std::vector<int> *arr = new std::vector<int>();
    while (head != nullptr) {
        arr->push_back(head->val);
        head = head->next;
    }
    return *arr;
}
