# [Python/Java/JavaScript/Go] Inorder successor in a binary search tree

> slug: by-himymben-vouy
> date: 2022-05-15
> tags: Go, Java, JavaScript, Python, Python3
> question: Inorder Successor in BST (inorder-successor-in-bst)
> url: https://leetcode.cn/problems/inorder-successor-in-bst/solutions/g2C95x/by-himymben-vouy/

---
### Approach
[Same as [面试题 04.06](https://leetcode.cn/problems/successor-lcci/)]
An inorder traversal of a binary search tree visits nodes from smallest to largest.
The inorder successor of a node is therefore the smallest node greater than it. In a BST:
If the node has a right subtree, the successor is the leftmost node in that subtree. Otherwise, it is the nearest ancestor reached through a left-child descent. If neither exists, the successor is null.
Keep track of the parent when descending into a left subtree.

### Code

```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        parent, node = None, root
        while node:
            if node.val > p.val:
                parent, node = node, node.left
            elif node.val < p.val:
                node = node.right
            elif node.right:
                node = node.right
                while node.left:
                    node = node.left
                return node
            else:
                return parent
        return None
```
```Java []
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        TreeNode parent = null, node = root;
        while(node != null) {
            if(node.val > p.val) {
                parent = node;
                node = node.left;
            } else if(node.val < p.val) {
                node = node.right;
            } else if(node.right != null) {
                node = node.right;
                while(node.left != null) {
                    node = node.left;
                }
                return node;
            } else {
                return parent;
            }
        }
        return parent;
    }
}
```
```JavaScript []
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @return {TreeNode}
 */
var inorderSuccessor = function(root, p) {
    let parent = null, node = root
    while(node != null) {
        if(node.val > p.val) {
            [parent, node] = [node, node.left]
        } else if(node.val < p.val) {
            node = node.right
        } else if(node.right != null) {
            node = node.right
            while(node.left != null) {
                node = node.left
            }
            return node
        } else {
            return parent
        }
    }
    return parent
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
func inorderSuccessor(root *TreeNode, p *TreeNode) (parent *TreeNode) {
    for node := root; node != nil; {
        if node.Val > p.Val {
            parent, node = node, node.Left
        } else if node.Val < p.Val {
            node = node.Right
        } else if node.Right != nil {
            node = node.Right
            for node.Left != nil {
                node = node.Left
            }
            return node
        } else {
            return
        }
    }
    return
}
```
```Python3 [v1-recursive-Py]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        return (res if (res := self.inorderSuccessor(root.left, p)) else root if root.val > p.val else self.inorderSuccessor(root.right, p)) if root else root
```
```Java [v1-recursive-Java]
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        return root == null ? root : (root.val > p.val ? (inorderSuccessor(root.left, p) == null ? root : inorderSuccessor(root.left, p)): inorderSuccessor(root.right, p));
    }
}
```
```JavaScript [v1-recursive-JavaScript]
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @return {TreeNode}
 */
var inorderSuccessor = function(root, p) {
    return root == null ? root : (root.val > p.val ? (inorderSuccessor(root.left, p) != null ? inorderSuccessor(root.left, p) : root) : inorderSuccessor(root.right, p))
};
```
```Go [v1-recursive-Go]
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func inorderSuccessor(root *TreeNode, p *TreeNode) (ans *TreeNode) {
    if root == nil {
        return
    }
    if root.Val > p.Val {
        if res := inorderSuccessor(root.Left, p); res != nil {
            return res
        }
        return root
    }
    return inorderSuccessor(root.Right, p)
}
```
