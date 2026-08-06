# [Python/Go] 递归维护前缀和个数 

> slug: pythongo-di-gui-wei-hu-qian-zhui-he-ge-s-dtls
> date: 2021-11-15
> tags: Go, Python, Python3
> question: Paths with Sum LCCI (paths-with-sum-lcci)
> url: https://leetcode.cn/problems/paths-with-sum-lcci/solutions/IBwy4i/pythongo-di-gui-wei-hu-qian-zhui-he-ge-s-dtls/

---
```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        counts = Counter([0])
        self.ans = 0
        def dfs(node, prev):
            if not node:
                return
            prev += node.val
            self.ans += counts[prev - sum]
            counts[prev] += 1
            dfs(node.left, prev)
            dfs(node.right, prev)
            counts[prev] -= 1
            prev -= node.val

        dfs(root, 0)
        return self.ans
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
func pathSum(root *TreeNode, sum int) int {
    cnts := map[int]int{0:1}
    var dfs func(*TreeNode, int) int
    dfs = func(node *TreeNode, prev int) int {
        ans := 0
        if node != nil {
            prev += node.Val
            ans += cnts[prev - sum]
            cnts[prev]++
            ans += dfs(node.Left, prev)
            ans += dfs(node.Right, prev)
            cnts[prev]--
        }
        return ans
    }
    return dfs(root, 0)
}
```