# [Python/C] 中序遍历迭代器

> Author: Benhao
> Date: 2024-02-10
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [94. 二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal/description/)

[TOC]

# 思路

> 中序遍历模拟

# 解题方法

> 中序遍历：优先左节点，然后自己，最后右节点
> 先序遍历: 优先自己，然后左节点，最后右节点
> 后序遍历: 优先左节点，然后右节点，最后自己

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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return
            yield from dfs(node.left)
            yield node.val
            yield from dfs(node.right)
        
        return [v for v in dfs(root)]
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
 * Note: The returned array must be malloced, assume caller calls free().
 */

int arr[100];
int idx;

void dfs(struct TreeNode *node) {
    if (!node) {
        return;
    }
    dfs(node->left);
    arr[idx++] = node->val;
    dfs(node->right);
}

int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    bzero(arr, sizeof(int) * 100);
    idx = 0;
    dfs(root);
    *returnSize = idx;
    return arr;
}
```
