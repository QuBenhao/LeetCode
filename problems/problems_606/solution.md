# [Python/Java/JavaScript/Go] 递归

> slug: pythonjavajavascriptgo-by-himymben-6400
> date: 2022-03-19
> tags: Go, Java, JavaScript, Python, Python3
> question: Construct String from Binary Tree (construct-string-from-binary-tree)
> url: https://leetcode.cn/problems/construct-string-from-binary-tree/solutions/p3bruk/pythonjavajavascriptgo-by-himymben-6400/

---
### 解题思路
在有左孩子或右孩子时，左边的括号才会被添加。
在有右孩子的时候，右边的括号才会被添加。
其他和先序遍历没有区别。

### 代码

```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:        
        return "" if not root else ("{}({})({})".format(root.val, self.tree2str(root.left), self.tree2str(root.right)) if root.right else ("{}({})".format(root.val, self.tree2str(root.left)) if root.left else str(root.val)))
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
    private StringBuilder sb;
    public String tree2str(TreeNode root) {
        sb = new StringBuilder();
        dfs(root);
        return sb.toString();
    }

    private void dfs(TreeNode node) {
        if(node != null) {
            sb.append(node.val);
            boolean hasLeft = node.left != null || node.right != null, hasRight = node.right != null;
            if(hasLeft) {
                sb.append("(");
                dfs(node.left);
                sb.append(")");
            }
            if(hasRight) {
                sb.append("(");
                dfs(node.right);
                sb.append(")");
            }
        }
    }
}
```
```JavaScript []
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {string}
 */
var tree2str = function(root) {
    const res = new Array()
    dfs = function(node) {
        if(node != null) {
            res.push(node.val)
            const hasLeft = node.left != null || node.right != null, hasRight = node.right != null
            if(hasLeft) {
                res.push("(")
                dfs(node.left)
                res.push(")")
            }
            if(hasRight) {
                res.push("(")
                dfs(node.right)
                res.push(")")
            }
        }
    }
    dfs(root)
    return res.join("")
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
func tree2str(root *TreeNode) string {
    ans := &strings.Builder{}
    var dfs func(node *TreeNode)
    dfs = func(node *TreeNode) {
        if node != nil {
            ans.WriteString(strconv.Itoa(node.Val))
            hasLeft, hasRight := node.Left != nil || node.Right != nil, node.Right != nil
            if hasLeft {
                ans.WriteByte('(')
                dfs(node.Left)
                ans.WriteByte(')')
            }
            if hasRight {
                ans.WriteByte('(')
                dfs(node.Right)
                ans.WriteByte(')')
            }
        }
    }
    dfs(root)
    return ans.String()
}
```