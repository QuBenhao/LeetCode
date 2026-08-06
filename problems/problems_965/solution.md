# [Python/Java/TypeScript/Go] 模拟

> slug: pythonjavajavascriptgo-by-himymben-tvtg
> date: 2022-05-23
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Univalued Binary Tree (univalued-binary-tree)
> url: https://leetcode.cn/problems/univalued-binary-tree/solutions/y0KgCe/pythonjavajavascriptgo-by-himymben-tvtg/

---
### 解题思路
就遍历树就行

### 代码

```Python3 [v1-Py迭代器写法]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        v = root.val

        def dfs(node):
            if node:
                yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)
        
        return all(v == other for other in dfs(root))
```
```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        v = root.val
        def dfs(node):
            return node is None or (node.val == v and dfs(node.left) and dfs(node.right))
        return dfs(root)
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
    public boolean isUnivalTree(TreeNode root) {
        return dfs(root, root.val);
    }

    private boolean dfs(TreeNode node, int val) {
        return node == null || (node.val == val && dfs(node.left, val) && dfs(node.right, val));
    }
}
```
```TypeScript []
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function isUnivalTree(root: TreeNode | null): boolean {
    const val: number = root?.val
    const dfs = (root: TreeNode | null) : boolean => {
        return root == null || (root.val == val && dfs(root.left) && dfs(root.right))
    }
    return dfs(root)
};
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
func isUnivalTree(root *TreeNode) bool {
    v := root.Val
    var dfs func(node *TreeNode) bool
    dfs = func(node *TreeNode) bool {
        if node != nil {
            return node.Val == v && dfs(node.Left) && dfs(node.Right)
        }
        return true
    }
    return dfs(root)
}
```