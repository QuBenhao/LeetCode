# [Python/Go/C] 先序+后序

> slug: pythongoc-xian-xu-hou-xu-by-himymben-qtu4
> date: 2024-02-22
> tags: Tree, C, Go, Java, Python3, TypeScript
> question: Construct Binary Tree from Preorder and Postorder Traversal (construct-binary-tree-from-preorder-and-postorder-traversal)
> url: https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal/solutions/zfgWwh/pythongoc-xian-xu-hou-xu-by-himymben-qtu4/

---

> Problem: [889. 根据前序和后序遍历构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/)

[TOC]

# 思路

> 按根节点在后序中对左右子树进行拆分

# 解题方法

> 先序、后序拆分左右子树

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
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        if len(preorder) > 1:
            idx = postorder.index(preorder[1])
            root.left = self.constructFromPrePost(preorder[1:idx+2], postorder[:idx+1])
            if idx + 2 < len(preorder):
                root.right = self.constructFromPrePost(preorder[idx+2:], postorder[idx+1:-1])
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
func constructFromPrePost(preorder []int, postorder []int) *TreeNode {
    root := &TreeNode{preorder[0], nil, nil}
    if len(preorder) > 1 {
        idx := 0
        for i, v := range postorder {
            if v == preorder[1] {
                idx = i
                break
            }
        }
        root.Left = constructFromPrePost(preorder[1:idx+2], postorder[:idx+1])
        if idx + 2 < len(preorder) {
            root.Right = constructFromPrePost(preorder[idx+2:], postorder[idx+1:len(postorder)-1])
        }
    }
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
struct TreeNode* constructFromPrePost(int* preorder, int preorderSize, int* postorder, int postorderSize) {
    if (preorderSize == 0) {
        return NULL;
    }
    struct TreeNode *root = malloc(sizeof(struct TreeNode));
    root->val = preorder[0];
    root->left = NULL;
    root->right = NULL;
    if (preorderSize > 1) {
        int idx;
        for (int i = 0; i < postorderSize; i++) {
            if (postorder[i] == preorder[1]) {
                idx = i;
                break;
            }
        }
        root->left = constructFromPrePost(preorder + 1, idx + 1, postorder, idx + 1);
        if (idx + 2 < preorderSize) {
            root->right = constructFromPrePost(preorder + idx + 2, preorderSize - 2 - idx, postorder + idx + 1, postorderSize -2 - idx);
        }
    }
    return root;
}
```
  
