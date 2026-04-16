# [Python/Java/TypeScript/Go] DFS

> Author: Benhao
> Date: 2022-08-04
> Upvotes: 22
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
按题目含义递归处理

### 代码

```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(node, d):
            if not node:
                return
            if d == depth - 1:
                node.left = TreeNode(val, node.left, None)
                node.right = TreeNode(val, None, node.right)
                return
            dfs(node.left, d + 1)
            dfs(node.right, d + 1)
        
        if depth == 1:
            return TreeNode(val, root, None)
        dfs(root, 1)
        return root
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
    public TreeNode addOneRow(TreeNode root, int val, int depth) {
        if (root == null) {
            return root;
        } else if (depth == 1) {
            return new TreeNode(val, root, null);
        } else if (depth == 2) {
            root.left = new TreeNode(val, root.left, null);
            root.right = new TreeNode(val, null, root.right);
            return root;
        }
        addOneRow(root.left, val, --depth);
        addOneRow(root.right, val, depth);
        return root;
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

function addOneRow(root: TreeNode | null, val: number, depth: number): TreeNode | null {
    if (root == null) {
        return root
    }
    if (depth == 1) {
        return new TreeNode(val, root, null)
    } else if (depth == 2) {
        root.left = new TreeNode(val, root.left, null)
        root.right = new TreeNode(val, null, root.right)
        return root
    }
    addOneRow(root.left, val, --depth)
    addOneRow(root.right, val, depth)
    return root
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
func addOneRow(root *TreeNode, val int, depth int) *TreeNode {
    if root != nil {
        if (depth == 1) {
            return &TreeNode{val, root, nil}
        } else if (depth == 2) {
            root.Left = &TreeNode{val, root.Left, nil}
            root.Right = &TreeNode{val, nil, root.Right}
        } else {
            addOneRow(root.Left, val, depth - 1)
            addOneRow(root.Right, val, depth - 1)
        }
    }
    return root
}
```