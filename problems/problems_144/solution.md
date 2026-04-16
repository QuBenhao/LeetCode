# [Python/C/Go] 迭代器

> Author: Benhao
> Date: 2024-02-11
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [144. 二叉树的前序遍历](https://leetcode.cn/problems/binary-tree-preorder-traversal/description/)

[TOC]

# 思路

> 前序遍历模拟题

# 解题方法

> 前序遍历：先自己，再左节点，最后右节点

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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return
            yield node.val
            yield from dfs(node.left)
            yield from dfs(node.right)
        
        return [v for v in dfs(root)]
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
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int arr[100];
int idx;

void dfs(struct TreeNode *node) {
    if (!node)
        return;
    arr[idx++] = node->val;
    dfs(node->left);
    dfs(node->right);
}

int* preorderTraversal(struct TreeNode* root, int* returnSize) {
    bzero(arr, sizeof(int) * 100);
    idx = 0;
    dfs(root);
    *returnSize = idx;
    return arr;
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
func preorderTraversal(root *TreeNode) []int {
    var walk func(node *TreeNode, ch chan int)
    walk = func(node *TreeNode, ch chan int) {
        if node == nil {
            return
        }
        ch <- node.Val
        walk(node.Left, ch)
        walk(node.Right, ch)
    }
    f := func(node *TreeNode, ch chan int) {
        walk(node, ch)
        close(ch)
    }
    c := make(chan int)
    arr := make([]int, 0)
    go f(root, c)
    for v := range c {
        arr = append(arr, v)
    }
    return arr
}
```
  
