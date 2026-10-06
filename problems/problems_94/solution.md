# [Python/C] Inorder traversal iterator

> Author: Benhao
> Date: 2024-02-10
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [94. 二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal/description/)

[TOC]

# Intuition

> Simulate inorder traversal

# Approach

> Inorder traversal: visit the left node, then the current node, and finally the right node.
> Preorder traversal: visit the current node, then the left node, and finally the right node.
> Postorder traversal: visit the left node, then the right node, and finally the current node.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
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
