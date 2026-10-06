# [Python/Go/C] Concise recursion

> Author: Benhao
> Date: 2024-02-26
> Upvotes: 3
> Tags: Tree, Depth-First Search, C, Go, Java, Python3, TypeScript

---


> Problem: [938. 二叉搜索树的范围和](https://leetcode.cn/problems/range-sum-of-bst/description/)

[TOC]

# Intuition

> In a binary search tree, add the current node to the sum if it is in range. If it exceeds the lower bound, search the right subtree; if it is below the upper bound, search the left subtree

# Approach

> Process recursively

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(1)$



# Code
```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        ans = -root.val
        if root.val >= low:
            ans += root.val + self.rangeSumBST(root.left, low, high)
        if root.val <= high:
            ans += root.val + self.rangeSumBST(root.right, low, high)
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
func rangeSumBST(root *TreeNode, low int, high int) int {
    if root == nil {
        return 0
    }
    ans := -root.Val
    if root.Val >= low {
        ans += root.Val + rangeSumBST(root.Left, low, high)
    }
    if root.Val <= high {
        ans += root.Val + rangeSumBST(root.Right, low, high)
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
int rangeSumBST(struct TreeNode* root, int low, int high) {
    if (!root) {
        return 0;
    }
    int ans = -root->val;
    if (root->val >= low) {
        ans += root->val + rangeSumBST(root->left, low, high);
    }
    if (root->val <= high) {
        ans += root->val + rangeSumBST(root->right, low, high);
    }
    return ans;
}
```
  
