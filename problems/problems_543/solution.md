# [Python/Go/C] Recursive approach

> Author: Benhao
> Date: 2024-02-19
> Upvotes: 2
> Tags: Tree, Depth-First Search, Binary Tree, C, Go, Java, Python3, TypeScript

---


> Problem: [543. 二叉树的直径](https://leetcode.cn/problems/diameter-of-binary-tree/description/)

[TOC]

# Intuition

> At the current node, consider two kinds of longest paths:
>> 1. A path ending at the current node:
>>> a. The longest path ending at the left child + the current node
>>> b. The longest path ending at the right child + the current node
>>> Take the larger of the two.
>> 2. A path that avoids the current node or connects both subtrees through it:
>>> a. The maximum diameter in the left subtree
>>> b. The maximum diameter in the right subtree
>>> c. The longest path ending at the left child + the current node + the longest path ending at the right child
>>> Each subtree's maximum diameter is at least as long as its longest path ending at that child, so those paths do not need separate comparisons here.

# Approach

> Recursion

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return 0, 0
            left, left_n = helper(node.left)
            right, right_n = helper(node.right)
            return max(left + 1, right + 1), max(left_n, right_n, left + right + 1)
        
        return helper(root)[1] - 1
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
func max(vals ...int) int {
    ans := vals[0]
    for _, v := range vals {
        if v > ans {
            ans = v
        }
    }
    return ans
} 

func diameterOfBinaryTree(root *TreeNode) int {
    var helper func(node *TreeNode) []int
    helper = func(node *TreeNode) []int {
        if node == nil {
            return []int{0, 0}
        }
        left := helper(node.Left)
        right := helper(node.Right)
        return []int{max(left[0] + 1, right[0] + 1), max(left[1], right[1], left[0] + right[0] + 1)}
    }

    return helper(root)[1] - 1
}
```

# Intuition
Once the code above makes sense, we can simplify the recursive return value by maintaining a single maximum.
Let the recursive function return the longest path ending at the current node, while maintaining the overall longest path during recursion. We no longer need to return lengths of paths that do not end at the current node. Their lengths cannot change later, so only whether they improve the final answer matters.

# Code

```C []
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
#define MAX(a, b) ((a) > (b) ? (a) : (b))

int helper(struct TreeNode *node, int *ans) {
    if (!node) {
        return 0;
    }
    int left = helper(node->left, ans);
    int right = helper(node->right, ans);

    *ans = MAX(*ans, left + right + 1);
    return MAX(left, right) + 1;
}

int diameterOfBinaryTree(struct TreeNode* root) {
    int ans = 0;
    helper(root, &ans);
    return ans - 1;
}
```
