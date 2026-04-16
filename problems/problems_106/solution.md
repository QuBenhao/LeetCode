# [Python/Go/C] 简洁递归

> Author: Benhao
> Date: 2024-02-21
> Upvotes: 4
> Tags: Tree, C, Go, Java, Python3, TypeScript

---


> Problem: [106. 从中序与后序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/)

[TOC]

# 思路

> 从后序遍历的最后一个确定当前节点的值，再已中序遍历该值分割出左右节点的值列表进行递归处理

# 解题方法

> 与前序序列+中序序列类似

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
