# [Python/Go/Java/Cpp] 归并排序

> Author: Benhao
> Date: 2024-03-16
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [21. 合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/description/)

[TOC]

# 思路

> 每次取两个链表中更小的一个，向后移动比较

# 解题方法

> 归并排序

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        while list1 and list2:
            if list1.val < list2.val:
                node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                node.next = ListNode(list2.val)
                list2 = list2.next
            node = node.next
        remain = list1 or list2
        while remain:
            node.next = ListNode(remain.val)
            node = node.next
            remain = remain.next
        return dummy.next
```
```Golang []
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	dummy := &ListNode{}
	for cur := dummy; list1 != nil || list2 != nil; cur = cur.Next {
		if list1 != nil && (list2 == nil || list2.Val >= list1.Val) {
			cur.Next = &ListNode{Val: list1.Val}
			list1 = list1.Next
		} else {
			cur.Next = &ListNode{Val: list2.Val}
			list2 = list2.Next
		}
	}
	return dummy.Next
}
```
```Java []
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode();
        for (ListNode node = dummy; list1 != null || list2 != null; node = node.next) {
            if (list2 != null && (list1 == null || list1.val > list2.val)) {
                node.next = new ListNode(list2.val);
                list2 = list2.next;
            } else {
                node.next = new ListNode(list1.val);
                list1 = list1.next;
            }
        }
        return dummy.next;
    }
}
```
```Cpp []
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* dummy = new ListNode(), *node = dummy;
        while (list1 != nullptr or list2 != nullptr) {
            if (list2 != nullptr && (list1 == nullptr || list1->val > list2->val)) {
                node->next = new ListNode(list2->val);
                list2 = list2->next;
            } else if (list1 != nullptr) {
                node->next = new ListNode(list1->val);
                list1 = list1->next;
            }
            node = node->next;
        }
        return dummy->next;     
    }
};
```
  
