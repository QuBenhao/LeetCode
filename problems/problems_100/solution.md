# [Python/C/Go/Java/Ts] 一行递归

> Author: Benhao
> Date: 2024-03-07
> Upvotes: 3
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [100. 相同的树](https://leetcode.cn/problems/same-tree/description/)

[TOC]

# 思路

> 模拟

# 解题方法

> 两个树一样首先根节点的值一致，左子树要一致，右子树要一致。递归处理即可

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return (not p and not q) or (p is not None and q is not None and p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
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
bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    return (p == NULL && q == NULL) || (p && q && p->val == q->val && isSameTree(p->left, q->left) && isSameTree(p->right, q->right));
}
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
func isSameTree(p *TreeNode, q *TreeNode) bool {
    return (p == nil && q == nil) || (p != nil && q != nil && p.Val == q.Val && isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right))
}
```
```Java []
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        return (p == null && q == null) || (p != null && q != null && p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right));
    }
}
```
```TypeScript []
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
    return (p == null && q == null) || (p != null && q != null && p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right))
};
```
