# [Python/Go/C] Recursion overview

> Author: Benhao
> Date: 2024-02-20
> Upvotes: 2
> Tags: Tree, C, Go, Java, Python3, TypeScript

---


> Problem: [105. 从前序与中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)

[TOC]

# Intuition

> The first value in preorder traversal is the root value. In inorder traversal, values to the left of the root belong to the left subtree, and values to the right belong to the right subtree. Construct the tree recursively.

# Approach

> Split the values into left and right subtrees at the root, then process them recursively.

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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
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
func buildTree(preorder []int, inorder []int) *TreeNode {
    if len(inorder) == 0 {
        return nil
    }
    root := &TreeNode{preorder[0], nil, nil}
    idx := 0
    for ; idx < len(inorder); idx++ {
        if inorder[idx] == preorder[0] {
            break
        }
    }
    root.Left = buildTree(preorder[1:idx+1], inorder[:idx])
    root.Right = buildTree(preorder[idx+1:], inorder[idx+1:])
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
struct TreeNode* buildTree(int* preorder, int preorderSize, int* inorder, int inorderSize) {
    if (inorderSize == 0) {
        return NULL;
    }
    struct TreeNode *root = malloc(sizeof(struct TreeNode));
    root->val = preorder[0];
    int idx;
    for (idx = 0; idx < inorderSize; idx++) {
        if (inorder[idx] == preorder[0]) {
            break;
        }
    }
    root->left = buildTree(preorder+1,idx,inorder,idx);
    root->right = buildTree(preorder+idx+1,preorderSize-1-idx,inorder+idx+1,inorderSize-1-idx);
    return root;
}
```
