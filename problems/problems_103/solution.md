# [Python/Go/C] BFS应用

> Author: Benhao
> Date: 2024-02-16
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [103. 二叉树的锯齿形层序遍历](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/description/)

[TOC]

# 思路

> 用层序遍历，但按奇偶层倒叙

# 解题方法

> BFS

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        queue, cur = deque([root]), 0
        while queue:
            length, tmp = len(queue), deque()
            for i in range(length):
                node = queue.popleft()
                if not cur:
                    tmp.append(node.val)
                else:
                    tmp.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(list(tmp))
            cur ^= 1
        return ans
```
```Go []
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func zigzagLevelOrder(root *TreeNode) [][]int {
    ans := [][]int{}
    if root == nil {
        return ans
    }
    queue := []*TreeNode{root}
    for i := 0; len(queue) > 0; i++ {
        length := len(queue)
        cur := make([]int, length)
        ans = append(ans, cur)
        for j := 0; j < length; j++ {
            if i % 2 != 0 {
                cur[length - 1 - j] = queue[j].Val
            } else {
                cur[j] = queue[j].Val
            }
            if queue[j].Left != nil {
                queue = append(queue, queue[j].Left)
            }
            if queue[j].Right != nil {
                queue = append(queue, queue[j].Right)
            }
        }
        queue = queue[length:]
    }
    return ans
}
```
```C []
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

int maxDepth;

void dfs(struct TreeNode *node, int depth) {
    if (!node)
        return;
    if (depth > maxDepth) {
        maxDepth = depth;
    }
    dfs(node->left, depth + 1);
    dfs(node->right, depth + 1);
}

typedef struct listNode {
    struct listNode *next;
    void *data;
} ListNode;

typedef struct {
    ListNode *head;
    ListNode *tail;
    int length;
} Queue;

void *dequeue(Queue *queue) {
    ListNode *node = queue->head;
    void *data = node->data;
    queue->head = node->next;
    free(node);
    queue->length--;
    if (!queue->length) {
        queue->tail = NULL;
    }
    return data;
}

void enqueue(Queue *queue, void *data) {
    if (!data)
        return;
    ListNode *node = malloc(sizeof(ListNode));
    node->next = NULL;
    node->data = data;
    if (!queue->tail) {
        queue->head = node;
    } else {
        queue->tail->next = node;
    }
    queue->tail = node;
    queue->length++;
}

int** zigzagLevelOrder(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {
    maxDepth = 0;
    dfs(root, 1);
    *returnSize = maxDepth;
    if (!root)
        return NULL;
    int **ans = malloc(sizeof(int *) * maxDepth);
    *returnColumnSizes = malloc(sizeof(int) * maxDepth);
    ListNode *rNode = malloc(sizeof(ListNode));
    rNode->next = NULL;
    rNode->data = root;
    Queue queue = {.head = rNode, .tail = rNode, .length = 1};
    for (int i = 0; queue.length > 0; i++) {
        int len = queue.length;
        (*returnColumnSizes)[i] = len;
        ans[i] = malloc(sizeof(int) * len);
        for (int j = 0; j < len; j++) {
            struct TreeNode *node = (struct TreeNode *) dequeue(&queue);
            ans[i][i % 2 != 0 ? len - 1 - j:j] = node->val;
            enqueue(&queue, node->left);
            enqueue(&queue, node->right);
        }
    }
    return ans;
}
```
