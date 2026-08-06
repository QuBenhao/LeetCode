# [Python/C/Go] 前序遍历迭代器

> slug: pythoncgo-qian-xu-bian-li-die-dai-qi-by-y0ue9
> date: 2024-02-18
> tags: C, Go, Java, Python3, TypeScript
> question: N-ary Tree Preorder Traversal (n-ary-tree-preorder-traversal)
> url: https://leetcode.cn/problems/n-ary-tree-preorder-traversal/solutions/oGHJYL/pythoncgo-qian-xu-bian-li-die-dai-qi-by-y0ue9/

---

> Problem: [589. N 叉树的前序遍历](https://leetcode.cn/problems/n-ary-tree-preorder-traversal/description/)

[TOC]

# 思路

> 标准的前序遍历

# 解题方法

> 先加入当前节点的值，再从左至右递归处理子节点

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(node):
            if not node:
                return
            yield node.val
            for child in node.children:
                yield from dfs(child)
        
        return [v for v in dfs(root)]
```
```Go []
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

func preorder(root *Node) []int {
    var walk func(node *Node, ch chan int)
    walk = func(node *Node, ch chan int) {
        if node == nil {
            return
        }
        ch <- node.Val
        for _, child := range node.Children {
            walk(child, ch)
        }
    }
    f := func(node *Node, ch chan int) {
        walk(node, ch)
        close(ch)
    }
    c := make(chan int)
    arr := make([]int, 0)
    go f(root, c)
    for v := range c {
        arr = append(arr, v)
    }
    return arr
}
```
```C []
/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     int numChildren;
 *     struct Node** children;
 * };
 */

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#define MAX_NODES 10000

void dfs(struct Node *node, int *result, int *idx) {
    result[(*idx)++] = node->val;
    for (int i = 0; i < node->numChildren; i++) {
        dfs(node->children[i], result, idx);
    }
}

int* preorder(struct Node* root, int* returnSize) {
    int *ans = malloc(sizeof(int) * MAX_NODES);
    *returnSize = 0;
    if (root) {
        dfs(root, ans, returnSize);
    }
    return ans;
}
```
  
