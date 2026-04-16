# [Python/Go/C] 递归思想

> Author: Benhao
> Date: 2024-02-19
> Upvotes: 2
> Tags: Tree, Depth-First Search, Binary Tree, C, Go, Java, Python3, TypeScript

---


> Problem: [543. 二叉树的直径](https://leetcode.cn/problems/diameter-of-binary-tree/description/)

[TOC]

# 思路

> 当前节点有两种可能的最大路径：
>> 1. 以当前路径为端点：
>>> a. 以左节点为端点的最大路径+当前节点
>>> b. 以右节点为端点的最大路径+当前节点
>>> 两者取大
>> 2. 不经过当前节点或以当前节点为折线:
>>> a. 左节点中的最大直径
>>> b. 右节点中的最大直径
>>> c. 以左节点为端点的最大路径+当前节点+以右节点为端点的最大路径
>>> 这里因为左右节点的最大直径一定不小于以左右节点为端点的最大路径，所以不用加入大小比较中

# 解题方法

> 递归

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

# 思路
理解了上面的代码以后，就可以理解如何用一个最大值简化递归返回。
我们将递归函数的返回定义改为以当前节点为端点的最大路径长度，而我们在递归过程中统一维护最大的可能路径。这样上一个思路中多余的不以当前节点为端点的路径的长度就不再需要被维护了，我们直接关心它们是否可以成为最终的答案就可以了，因为它们的长度以后也不会改变了。

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
