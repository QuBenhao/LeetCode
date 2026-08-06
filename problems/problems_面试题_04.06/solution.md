# [Python/Java/JavaScript/Go] 二叉搜索树的后继

> slug: pythonjavajavascriptgo-by-himymben-1h2p
> date: 2022-05-15
> tags: Go, Java, JavaScript, Python, Python3
> question: Successor LCCI (successor-lcci)
> url: https://leetcode.cn/problems/successor-lcci/solutions/ZxsLcp/pythonjavajavascriptgo-by-himymben-1h2p/

---
### 解题思路
二叉搜索树的中序遍历，节点是从小到大依次排列的。
那么二叉搜索树中的节点的中序后继节点，就是比它大的最小的那个，这在BST中体现为，
若节点存在右子树，那么该最小值为右子树的最左叶节点；若无右子树，该最小值为进左子树时的父节点；再没有就是空了。
我们维护一个进左子树时的父节点即可。

### 代码

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
```Python3 [v1-递归写法Py]
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
```Java [v1-递归写法Java]
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
```JavaScript [v1-递归写法JavaScript]
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
```Go [v1-递归写法Go]
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