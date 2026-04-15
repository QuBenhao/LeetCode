# [Python/Java/TypeScript/Go] 递归

> Author: Benhao
> Date: 2022-05-30
> Upvotes: 17
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
当前为叶子结点，则累加值左移一位并加上当前叶子节点的值。
当前不为叶子节点，累加值左移一位并加上当前节点的值，然后以新的累加值向下递归。

### 代码

```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cur):
            return ((cur << 1) + node.val if not node.left and not node.right else dfs(node.left, nxt := (cur << 1) + node.val) + dfs(node.right, nxt)) if node else 0
        
        return dfs(root, 0)
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
    public int sumRootToLeaf(TreeNode root) {
        return dfs(root, 0);
    }

    private int dfs(TreeNode node, int cur) {
        return node == null ? 0 : node.left == null && node.right == null ? (cur << 1) + node.val : dfs(node.left, (cur << 1) + node.val) + dfs(node.right, (cur << 1) + node.val);
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

function sumRootToLeaf(root: TreeNode | null): number {
    const dfs = (node: TreeNode | null, cur: number): number => {
        return node == null ? 0 : node.left == null && node.right == null ? (cur << 1) + node.val : dfs(node.left, (cur << 1) + node.val) + dfs(node.right, (cur << 1) + node.val)
    }
    return dfs(root, 0)
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
func sumRootToLeaf(root *TreeNode) int {
    var dfs func(node *TreeNode, cur int) int
    dfs = func(node *TreeNode, cur int) int {
        if node == nil {
            return 0
        }
        nxt := (cur << 1) + node.Val
        if node.Left == nil && node.Right == nil {
            return nxt
        }
        return dfs(node.Left, nxt) + dfs(node.Right, nxt)
    }
    return dfs(root, 0)
}
```