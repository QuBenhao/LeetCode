# [Python3] Concise recursion

> Author: Benhao
> Date: 2024-02-09
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [236. 二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/)

[TOC]

# Intuition

> Tree recursion

# Approach

> Return the current node if it is null or one of the target nodes. Otherwise, inspect the results from its left and right children. If both are non-null, the current node is the common ancestor; otherwise, return whichever result is non-null (which can be written with or).

# Complexity

Time complexity:
> $O(n)$

Space complexity:
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
