# [Python/Java] dfs递归

> slug: pythonjava-dfsdi-gui-by-himymben-9098
> date: 2021-09-23
> tags: Java, Python, Python3
> question: Flatten a Multilevel Doubly Linked List (flatten-a-multilevel-doubly-linked-list)
> url: https://leetcode.cn/problems/flatten-a-multilevel-doubly-linked-list/solutions/6qH9u9/pythonjava-dfsdi-gui-by-himymben-9098/

---
### 解题思路
有child就往child优先递归，返回末尾节点，将末尾节点和node.next拼接成双向链表(扁平化)即可。

### 代码

```Python3 []
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def dfs(node):
            if not node:
                return
            if not node.child and not node.next:
                return node 
            elif node.child:
                last = dfs(node.child)
                if last:
                    last.next = node.next
                if node.next:
                    node.next.prev = last
                node.next = node.child
                node.child.prev = node
                node.child = None
                return dfs(last)
            else:
                return dfs(node.next)
        dfs(head)
        return head                    
```
```Java []
class Solution {
    public Node flatten(Node head) {
        dfs(head);
        return head;
    }

    public Node dfs(Node node){
        if(node == null || (node.child == null && node.next == null))
            return node;
        if(node.child != null){
            Node last = dfs(node.child);
            if(last != null)
                last.next = node.next;
            if(node.next != null)
                node.next.prev = last;
            node.next = node.child;
            node.child.prev = node;
            node.child = null;
            return dfs(last);
        }
        return dfs(node.next);
    }
}
```