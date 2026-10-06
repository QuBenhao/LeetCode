# [Python/Java/JavaScript/Go] Replace the next node and change the link!

> slug: pythonjavajavascript-ti-huan-xia-yi-jie-04thl
> date: 2021-11-01
> tags: Go, Java, JavaScript, Python, Python3
> question: Delete Node in a Linked List (delete-node-in-a-linked-list)
> url: https://leetcode.cn/problems/delete-node-in-a-linked-list/solutions/6CnbRB/pythonjavajavascript-ti-huan-xia-yi-jie-04thl/

---
### Approach
Honestly, this problem is poorly framed: you can only delete the next node after copying its value into the given node. This does not actually delete the intended object.

### Code

```Python3 []
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
```
```Java []
class Solution {
    public void deleteNode(ListNode node) {
        node.val = node.next.val;
        node.next = node.next.next;
    }
}
```
```JavaScript []
/**
 * @param {ListNode} node
 * @return {void} Do not return anything, modify node in-place instead.
 */
var deleteNode = function(node) {
    node.val = node.next.val;
    node.next = node.next.next;
};
```

```Go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteNode(node *ListNode) {
    *node = *node.Next
}
```
