# [Python/Java/TypeScript/Go] 模拟

> slug: pythonjavatypescriptgo-by-himymben-x7n0
> date: 2022-06-18
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: 循环有序列表的插入 (4ueAj6)
> url: https://leetcode.cn/problems/4ueAj6/solutions/koe19T/pythonjavatypescriptgo-by-himymben-x7n0/

---
### 解题思路
遍历链表，找到这么一个节点，满足以下之一即为插入位置：
1. 插入值在它的值和它的下一个的值之间
2. 下一个值为旋转点，插入值比前面的值大或者比下一个的值小

若没有找到必然是在头尾之间 (插入位置必然存在)

### 代码

```Python3 []
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        inst = Node(insertVal)
        if not head:
            inst.next = inst
            return inst
        node = head
        while node.next != head:
            if node.next.val >= insertVal >= node.val:
                break
            if node.next.val < node.val and (node.val <= insertVal or insertVal <= node.next.val):
                break
            node = node.next
        inst.next = node.next
        node.next = inst
        return head
```
```Java []
/*
// Definition for a Node.
class Node {
    public int val;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _next) {
        val = _val;
        next = _next;
    }
};
*/

class Solution {
    public Node insert(Node head, int insertVal) {
        Node inst = new Node(insertVal);
        if (head == null) {
            inst.next = inst;
            return inst;
        }
        Node node = head;
        while (node.next != head) {
            if (node.val <= insertVal && insertVal <= node.next.val) {
                break;
            }
            if (node.val > node.next.val && (insertVal >= node.val || insertVal <= node.next.val)) {
                break;
            }
            node = node.next;
        }
        inst.next = node.next;
        node.next = inst;
        return head;
    }
}
```
```TypeScript []
/**
 * Definition for node.
 * class Node {
 *     val: number
 *     next: Node | null
 *     constructor(val?: number, next?: Node) {
 *         this.val = (val===undefined ? 0 : val);
 *         this.next = (next===undefined ? null : next);
 *     }
 * }
 */

function insert(head: Node | null, insertVal: number): Node | null {
    const inst = new Node(insertVal, undefined)
    if (head == null) {
        inst.next = inst
        return inst
    }
    let node = head
    while (node.next != head) {
        if (node.val <= insertVal && insertVal <= node.next.val) {
            break
        }
        if (node.val > node.next.val && (node.val <= insertVal || insertVal <= node.next.val)) {
            break
        }
        node = node.next
    }
    inst.next = node.next
    node.next = inst
    return head
}
```
```Go []
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 * }
 */

func insert(aNode *Node, x int) *Node {
    inst := &Node{x, nil}
    if aNode == nil {
        inst.Next = inst
        return inst
    }
    node := aNode
    for node.Next != aNode {
        if node.Val <= x && x <= node.Next.Val {
            break
        }
        if node.Val > node.Next.Val && (node.Val <= x || x <= node.Next.Val) {
            break
        }
        node = node.Next
    }
    inst.Next = node.Next
    node.Next = inst
    return aNode
}
```