# 二叉树

## 前序遍历

```python
def preorder(root):
    res = []

    def dfs(node):
        if not node:
            return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return res
```

```go
package main

type TreeNode struct {
    Val   int
    Left  *TreeNode
    Right *TreeNode
}

func preorderTraversal(root *TreeNode) []int {
    res := []int{}
    var dfs func(*TreeNode)
    dfs = func(node *TreeNode) {
        if node == nil {
            return
        }
        res = append(res, node.Val)
        dfs(node.Left)
        dfs(node.Right)
    }
    dfs(root)
    return res
}
```

## 中序遍历

## 后序遍历