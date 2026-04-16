# [Python/Go] 简洁BFS

> Author: Benhao
> Date: 2024-02-14
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [102. 二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/description/)

[TOC]

# 思路

> 一层层遍历是标准的BFS

# 解题方法

> BFS模拟

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        ans = []
        while queue:
            length, first = len(queue), True
            for i in range(length):
                node = queue.popleft()
                if not node:
                    continue
                if first:
                    ans.append([node.val])
                    first = False
                else:
                    ans[-1].append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return ans
```
```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue, ans = deque([root]), []
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if not i:
                    ans.append([node.val])
                else:
                    ans[-1].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
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
func levelOrder(root *TreeNode) [][]int {
    ans := [][]int{}
    if root == nil {
        return ans
    }
    queue := []*TreeNode{root}
    for i := 0; len(queue) > 0; i++ {
        ans = append(ans, []int{})
        for j, length := 0, len(queue); j < length; j++ {
            node := queue[0]
            queue = queue[1:]
            ans[i] = append(ans[i], node.Val)
            if node.Left != nil {
                queue = append(queue, node.Left)
            }
            if node.Right != nil {
                queue = append(queue, node.Right)
            }
        }
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

int** levelOrder(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {
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
    Queue *queue = malloc(sizeof(Queue));
    queue->head = rNode;
    queue->tail = rNode;
    queue->length = 1;
    for (int i = 0; queue->length > 0; i++) {
        (*returnColumnSizes)[i] = queue->length;
        ans[i] = malloc(sizeof(int) * ((*returnColumnSizes)[i]));
        for (int j = 0; j < (*returnColumnSizes)[i]; j++) {
            struct TreeNode *node = (struct TreeNode *) dequeue(queue);
            ans[i][j] = node->val;
            enqueue(queue, node->left);
            enqueue(queue, node->right);
        }
    }
    free(queue);
    return ans;
}
```
