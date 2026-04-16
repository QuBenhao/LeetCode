# [Python3] 简洁递归

> Author: Benhao
> Date: 2024-02-09
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [236. 二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/)

[TOC]

# 思路

> 树的递归

# 解题方法

> 如果当前节点为空或者要找的节点，返回自身；否则我们从左子节点的答案和右子节点的答案中找，当前的答案为：左右都不空时公共祖先是自己，其他情况返回两者不空的那个（简写为or即可）

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        lc = self.lowestCommonAncestor(root.left, p, q)
        rc = self.lowestCommonAncestor(root.right, p, q)
        return root if lc and rc else lc or rc
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
struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    if (!root || root == p || root == q) {
        return root;
    }
    struct TreeNode *lc = lowestCommonAncestor(root->left, p, q), *rc = lowestCommonAncestor(root->right, p, q);
    return lc && rc ? root : (lc ? lc : rc);
}
```
