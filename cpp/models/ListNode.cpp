//
// Created by BenHao on 2024/5/21.
//

#include "ListNode.h"

ListNode *IntArrayToListNode(const std::vector<int> &arr) {
    ListNode dummy = ListNode();
    ListNode *p = &dummy;
    for (auto val : arr) {
        p->next = new ListNode(val);
        p = p->next;
    }
    p = dummy.next;
    dummy.next = nullptr; // Prevent memory leak
    return p;
}

std::vector<int> ListNodeToIntArray(ListNode *head) {
    auto arr = std::vector<int>();
    while (head != nullptr) {
        arr.push_back(head->val);
        head = head->next;
    }
    return arr;
}

ListNode *IntArrayToListNodeCycle(std::vector<int> &arr, int pos) {
    ListNode dummy = ListNode();
    ListNode *p = &dummy;
    ListNode *cycle = nullptr;
    for (size_t i = 0; i < arr.size(); ++i) {
        p->next = new ListNode(arr[i]);
        p = p->next;
        if (i == pos) {
            cycle = p;
        }
    }
    p->next = cycle;
    p = dummy.next;
    dummy.next = nullptr; // Prevent memory leak
    return p;
}

std::tuple<ListNode *, ListNode *>
IntArrayToIntersectionListNode(int iv, std::vector<int> &arr1, std::vector<int> &arr2, int idx_a, int idx_b) {
    auto headA = IntArrayToListNode(arr1);
    if (iv == 0 || idx_a == static_cast<int>(arr1.size()) || idx_b == static_cast<int>(arr2.size())) {
        return {headA, IntArrayToListNode(arr2)};
    }
    auto pa = headA;
    for (int i = 0; i < idx_a; i++) {
        pa = pa->next;
    }
    auto headB = idx_b == 0 ? pa : new ListNode(arr2[0]);
    auto pb = headB;
    for (int i = 1; i < idx_b - 1; i++) {
        pb->next = new ListNode(arr2[i]);
        pb = pb->next;
    }
    pb->next = pa;
    return {headA, headB};
}