# [Python/Go/C] Concise recursion

> Author: Benhao
> Date: 2024-02-21
> Upvotes: 4
> Tags: Tree, C, Go, Java, Python3, TypeScript

---


> Problem: [106. 从中序与后序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/)

[TOC]

# Intuition

> Determine the current node's value from the last value in postorder traversal. Split the inorder traversal at that value into lists for the left and right subtrees, then process them recursively.

# Approach

> Similar to using preorder and inorder traversals together.

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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:idx],postorder[:idx])
        root.right = self.buildTree(inorder[idx+1:],postorder[idx:-1])
        return root
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
func buildTree(inorder []int, postorder []int) *TreeNode {
    if len(inorder) == 0 {
        return nil
    }
    val := postorder[len(postorder) - 1]
    root := &TreeNode{val, nil, nil}
    idx := 0
    for i, v := range inorder {
        if v == val {
            idx = i
            break
        }
    }
    root.Left = buildTree(inorder[:idx], postorder[:idx])
    root.Right = buildTree(inorder[idx+1:], postorder[idx:len(postorder) - 1])
    return root
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
struct TreeNode* buildTree(int* inorder, int inorderSize, int* postorder, int postorderSize) {
    if (inorderSize == 0) {
        return NULL;
    }
    struct TreeNode *root = malloc(sizeof(struct TreeNode));
    root->val = postorder[postorderSize - 1];
    int idx;
    for (int i = 0; i < inorderSize; i++) {
        if (inorder[i] == postorder[postorderSize - 1]) {
            idx = i;
            break;
        }
    }
    root->left = buildTree(inorder, idx, postorder, idx);
    root->right = buildTree(inorder + idx + 1, inorderSize - 1 - idx, postorder + idx, postorderSize - 1 - idx);
    return root;
}
```
