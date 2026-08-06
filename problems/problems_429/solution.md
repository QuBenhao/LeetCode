# [Python/Go/C] 标准BFS

> slug: pythongoc-biao-zhun-bfs-by-himymben-de6o
> date: 2024-02-17
> tags: C, Go, Java, Python3, TypeScript
> question: N-ary Tree Level Order Traversal (n-ary-tree-level-order-traversal)
> url: https://leetcode.cn/problems/n-ary-tree-level-order-traversal/solutions/AChU5W/pythongoc-biao-zhun-bfs-by-himymben-de6o/

---

> Problem: [429. N 叉树的层序遍历](https://leetcode.cn/problems/n-ary-tree-level-order-traversal/description/)

[TOC]

# 思路

> BFS应用题

# 解题方法

> BFS

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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        while queue:
            length = len(queue)
            ans.append([])
            for _ in range(length):
                node = queue.popleft()
                ans[-1].append(node.val)
                for child in node.children:
                    queue.append(child)
        return ans
```
```Go []
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

func levelOrder(root *Node) [][]int {
    ans := [][]int{}
    if root == nil {
        return ans
    }
    queue := []*Node{root}
    for len(queue) > 0 {
        length, cur := len(queue), []int{}
        for i := 0; i < length; i++ {
            cur = append(cur, queue[i].Val)
            for _, child := range queue[i].Children {
                queue = append(queue, child)
            }
        }
        ans = append(ans, cur)
        queue = queue[length:]
    }
    return ans
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
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
#define MAX_DEPTH 1000
#define MAX_NODE 10000

int** levelOrder(struct Node* root, int* returnSize, int** returnColumnSizes) {
    int **ans = (int **) malloc(sizeof(int *) * MAX_DEPTH);
    *returnColumnSizes = (int *) malloc(sizeof(int) * MAX_NODE);
    if (!root) {
        *returnSize = 0;
        return ans;
    }
    struct Node **queue = (struct Node **) malloc(sizeof(struct Node *) * MAX_NODE);
    int head = 0, tail = 0;
    queue[tail++] = root;
    int i;
    for (i = 0; head != tail; i++) {
        int length = tail - head;
        (*returnColumnSizes)[i] = length;
        ans[i] = (int *) malloc(sizeof(int) * length);
        for (int j = 0; j < length; j++) {
            struct Node *node = queue[head++];
            ans[i][j] = node->val;
            for (int c = 0; c < node->numChildren; c++) {
                queue[tail++] = node->children[c];
            }
        }
    }
    *returnSize = i;
    free(queue);
    return ans;
}
```
  
