# [Python/Java/JavaScript/Go] 替换下一节点 改变地址！

> slug: pythonjavajavascript-ti-huan-xia-yi-jie-04thl
> date: 2021-11-01
> tags: Go, Java, JavaScript, Python, Python3
> question: Delete Node in a Linked List (delete-node-in-a-linked-list)
> url: https://leetcode.cn/problems/delete-node-in-a-linked-list/solutions/6CnbRB/pythonjavajavascript-ti-huan-xia-yi-jie-04thl/

---
### 解题思路
这题说实话出的不好，因为你只能删掉下一个节点，把下一个节点的值都赋值给该节点。但是，这本质上并不是删掉想删的对象。

### 代码

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