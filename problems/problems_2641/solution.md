# [Python/C] DFS

> slug: python-dfs-by-himymben-vuce
> date: 2024-02-07
> tags: C, Go, Java, Python3, TypeScript
> question: Cousins in Binary Tree II (cousins-in-binary-tree-ii)
> url: https://leetcode.cn/problems/cousins-in-binary-tree-ii/solutions/GUlDW5/python-dfs-by-himymben-vuce/

---

> Problem: [2641. 二叉树的堂兄弟节点 II](https://leetcode.cn/problems/cousins-in-binary-tree-ii/description/)

[TOC]

# Intuition

> The sum of a node's cousins is the level sum minus the sum of the sibling group containing that node.

# Approach

> First compute level sums and sibling sums, then traverse again to assign the new values.

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
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ds = defaultdict(int)
        def dfs1(node, depth):
            if not node:
                return 0
            v = node.val
            ds[depth] += v
            node.val = dfs1(node.left, depth + 1) + dfs1(node.right, depth + 1)
            return v
        
        def dfs2(node, depth):
            if node.left:
                dfs2(node.left, depth + 1)
                node.left.val = ds[depth + 1] - node.val
            if node.right:
                dfs2(node.right, depth + 1)
                node.right.val = ds[depth + 1] - node.val
            node.val = 0

        dfs1(root, 0)
        dfs2(root, 0)
        return root
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


int dfs1(int *ds, struct TreeNode *node, int depth) {
    if (!node) {
        return 0;
    }
    int v = node->val;
    ds[depth] += v;
    node->val = dfs1(ds, node->left, depth + 1) + dfs1(ds, node->right, depth + 1);
    return v;
}

void dfs2(int *ds, struct TreeNode *node, int depth) {
    if (node->left) {
        dfs2(ds, node->left, depth + 1);
        node->left->val = ds[depth + 1] - node->val;
    }
    if (node->right) {
        dfs2(ds, node->right, depth + 1);
        node->right->val = ds[depth + 1] - node->val;
    }
    node->val = 0;
}

struct TreeNode* replaceValueInTree(struct TreeNode* root) {
    int ds[100000] = {0};

    dfs1(ds, root, 0);
    dfs2(ds, root, 0);
    return root;
}
```
  
