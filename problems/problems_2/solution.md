# [Python/Golang/Cpp/Java] 模拟

> Author: Benhao
> Date: 2024-03-07
> Upvotes: 14
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [2. 两数相加](https://leetcode.cn/problems/add-two-numbers/description/)

[TOC]

# 思路

> 以两个链表的遍历为循环是不够的，当我们出现最终位的进位时是比原两个链表更长的

# 解题方法

> 同时遍历两个链表，记录进位，最终返回结果

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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = 0
        n1, n2 = l1, l2
        head = ListNode()
        node = head
        while n1 or n2 or cur:
            if n1:
                cur += n1.val
                n1 = n1.next
            if n2:
                cur += n2.val
                n2 = n2.next
            node.next = ListNode(cur % 10)
            node = node.next
            cur //= 10
        return head.next
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *dummy = new ListNode();
        ListNode *node = dummy;
        for (int addition = 0; l1 != nullptr || l2 != nullptr || addition != 0; node = node->next) {
            int cur = addition;
            if (l1 != nullptr) {
                cur += l1->val;
                l1 = l1->next;
            }
            if (l2 != nullptr) {
                cur += l2->val;
                l2 = l2->next;
            }
            node->next = new ListNode(cur % 10);
            addition = cur / 10;
        }
        return dummy->next;
    }
};
```
```Golang []
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	dummy := &ListNode{}
	node := dummy
	for addition := 0; l1 != nil || l2 != nil || addition != 0; node = node.Next {
		cur := addition
		if l1 != nil {
			cur += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			cur += l2.Val
			l2 = l2.Next
		}
		node.Next = &ListNode{Val: cur % 10}
		addition = cur / 10
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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode();
        ListNode node = dummy;
        int addition = 0;
        while (l1 != null || l2 != null || addition != 0) {
            int cur = addition;
            if (l1 != null) {
                cur += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                cur += l2.val;
                l2 = l2.next;
            }
            node.next = new ListNode(cur % 10);
            node = node.next;
            addition = cur >= 10 ? 1 : 0;
        }
        return dummy.next;
    }
}
```

  
