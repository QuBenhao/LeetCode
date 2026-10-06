# [Python/Java/Go] Inorder traversal

> Author: Benhao
> Date: 2024-03-02
> Upvotes: 5
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [530. 二叉搜索树的最小绝对差](https://leetcode.cn/problems/minimum-absolute-difference-in-bst/description/)

[TOC]

# Intuition

> Use an inorder traversal and compare adjacent values to find the minimum difference.

# Approach

> Use an iterator with pairwise.

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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return
            yield from dfs(node.left)
            yield node.val
            yield from dfs(node.right)
        
        return min(b - a for a, b in pairwise(dfs(root)))
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
    int last;
    int ans;
    private void dfs(TreeNode node) {
        if (node == null) {
            return;
        }
        dfs(node.left);
        ans = Math.min(ans, node.val - last);
        last = node.val;
        dfs(node.right);
    }

    public int getMinimumDifference(TreeNode root) {
        last = -100000;
        ans = 100000;
        dfs(root);
        return ans;
    }
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
func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func getMinimumDifference(root *TreeNode) int {
    ans, last := 1000000, -1000000
    var dfs func(*TreeNode)
    dfs = func(node *TreeNode) {
        if (node == nil) {
            return
        }
        dfs(node.Left)
        ans = min(ans, node.Val - last)
        last = node.Val
        dfs(node.Right)
    }
    dfs(root)
    return ans
}
```
  
