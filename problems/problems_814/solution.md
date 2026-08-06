# [Python/Java/TypeScript/Go] 递归

> slug: pythonjavatypescriptgo-di-gui-by-himymbe-lvra
> date: 2022-07-20
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Binary Tree Pruning (binary-tree-pruning)
> url: https://leetcode.cn/problems/binary-tree-pruning/solutions/9le2Ev/pythonjavatypescriptgo-di-gui-by-himymbe-lvra/

---
### 解题思路
要剪掉所有全是0的分枝，我们可以递归看子树是否都为0，如果子树都为0即节点置为空。
如果子树都为空且自身是0就代表该节点可以被剪掉，返回空；
否则返回递归剪枝后的左子树和右子树构成的新树。

### 代码

```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        left, right = self.pruneTree(root.left), self.pruneTree(root.right)
        return None if not root.val and not left and not right else TreeNode(root.val, left, right)
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
    public TreeNode pruneTree(TreeNode root) {
        if (root == null) {
            return null;
        }
        TreeNode left = pruneTree(root.left), right = pruneTree(root.right);
        return root.val == 0 && left == null && right == null ? null : new TreeNode(root.val, left, right);
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

function pruneTree(root: TreeNode | null): TreeNode | null {
    if (root == null) {
        return null
    }
    const left: TreeNode | null = pruneTree(root.left), right : TreeNode | null = pruneTree(root.right)
    return root.val == 0 && left == null && right == null ? null : new TreeNode(root.val, left, right)
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
func pruneTree(root *TreeNode) *TreeNode {
    if root == nil {
        return nil
    }
    left, right := pruneTree(root.Left), pruneTree(root.Right)
    if root.Val == 0 && left == nil && right == nil {
        return nil
    }
    return &TreeNode{root.Val, left, right}
}
```