# [Python/Java/TypeScript/Go] 递归

> Author: Benhao
> Date: 2022-06-02
> Upvotes: 34
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
当前节点比删除值小，右子树的根变为右子树中删除；
当前节点比删除值大，左子树的根变为左子树中删除；
当前就是要被删的节点，如果它没有左子树或没有右子树，可以直接平移嫁接。
否则需要找到左子树最大值或右子树最小值作为新的根。

### 代码

```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root:
            if root.val < key:
                root.right = self.deleteNode(root.right, key)
            elif root.val > key:
                root.left = self.deleteNode(root.left, key)
            else:
                if not root.left or not root.right:
                    root = root.left if root.left else root.right
                else:
                    node = root.left
                    while node.right:
                        node = node.right
                    node.left = self.deleteNode(root.left, node.val)
                    node.right = root.right
                    root = node
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
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root != null) {
            if (root.val < key) {
                root.right = deleteNode(root.right, key);
            } else if (root.val > key) {
                root.left = deleteNode(root.left, key);
            } else {
                if (root.left == null || root.right == null) {
                    return root.left == null ? root.right : root.left;
                } else {
                    TreeNode node = root.left;
                    while (node.right != null) {
                        node = node.right;
                    }
                    node.left = deleteNode(root.left, node.val);
                    node.right = root.right;
                    root = node;
                }
            }
        }
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

function deleteNode(root: TreeNode | null, key: number): TreeNode | null {
    if (root != null) {
        if (root.val > key) {
            root.left = deleteNode(root.left, key)
        } else if (root.val < key) {
            root.right = deleteNode(root.right, key)
        } else {
            if (root.left == null || root.right == null) {
                root = root.left == null ? root.right : root.left
            } else {
                let node = root.left
                while (node.right != null) {
                    node = node.right
                }
                node.left = deleteNode(root.left, node.val)
                node.right = root.right
                root = node
            }
        }
    }
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
func deleteNode(root *TreeNode, key int) *TreeNode {
    if root != nil {
        if root.Val < key {
            root.Right = deleteNode(root.Right, key)
        } else if root.Val > key {
            root.Left = deleteNode(root.Left, key)
        } else {
            if root.Left == nil || root.Right == nil {
                if root.Left != nil {
                    root = root.Left
                } else {
                    root = root.Right
                }
            } else {
                node := root.Left
                for node.Right != nil {
                    node = node.Right
                }
                node.Left = deleteNode(root.Left, node.Val)
                node.Right = root.Right
                root = node
            }
        }
    }
    return root
}
```