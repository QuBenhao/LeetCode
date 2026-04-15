# [Python/Java/TypeScript/Go] DFS

> Author: Benhao
> Date: 2022-09-02
> Upvotes: 16
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
Ja\va语言打不出来了家人们（好像修复了）。
先给出一份WA的代码，一开始没注意路径是两点之间，
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            """
            返回最长路径以及根节点路径长度
            """
            if not node:
                # 根节点值, 根节点路径长度, 最长路径长度
                return (None, 0, 0)
            left, right = dfs(node.left), dfs(node.right)
            r = 1
            if node.val == left[0]:
                r += left[1]
            if node.val == right[0]:
                r += right[1]
            return (node.val, r, max(r, left[-1], right[-1]))

        return max(0, max(dfs(root)[1:]) - 1)
```
其实面对树上这种最大值，都是子节点的值返回以后和根节点计算后递归返回，和树形dp的思路差不多。
我们只需要维护一个根路径的值(一开始错误的地方)，维护一个根节点折线最大值即可。
因为路径是两点之间，所以根节点不能取折线，而是到根的最大值，这样递归返回可以继续作为折线的一半被使用。

### 代码

```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            """
            返回最长路径以及根节点路径长度
            """
            if not node:
                # 根节点值, 根节点不折线的最长路径长度, 最长路径长度
                return (None, 0, 0)
            left, right = dfs(node.left), dfs(node.right)
            return (node.val, max((lv := left[1] + 1 if node.val == left[0] else 1), (rv := right[1] + 1 if node.val == right[0] else 1)), max(lv + rv - 1, left[-1], right[-1]))

        return max(0, max(dfs(root)[1:]) - 1)
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
    public int longestUnivaluePath(TreeNode root) {
        int[] res = dfs(root);
        return Math.max(0, Math.max(res[1], res[2]) - 1);
    }

    private int[] dfs(TreeNode node) {
        if (node == null) {
            return new int[]{0, 0, 0};
        }
        int[] left = dfs(node.left), right = dfs(node.right);
        int lv = left[0] == node.val ? left[1] : 0;
        int rv = right[0] == node.val ? right[1] : 0;
        return new int[]{node.val, Math.max(lv, rv) + 1, Math.max(lv + rv + 1, Math.max(left[2], right[2]))};
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

function longestUnivaluePath(root: TreeNode | null): number {
    const dfs = (node: TreeNode | null): Array<number> => {
        if (node == null) {
            return [0, 0, 0]
        }
        const left: Array<number> = dfs(node.left), right: Array<number> = dfs(node.right)
        const lv: number = left[0] === node.val ? left[1]: 0, rv: number = right[0] === node.val ? right[1] : 0
        return [node.val, Math.max(lv, rv) + 1, Math.max(lv + rv + 1, left[2], right[2])]
    }

    const res: Array<number> = dfs(root)
    return Math.max(0, Math.max(res[1], res[2]) - 1)
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
func longestUnivaluePath(root *TreeNode) int {
    var dfs func(node *TreeNode) []int
    dfs = func(node *TreeNode) []int {
        if node == nil {
            return []int{0, 0, 0}
        }
        left, right := dfs(node.Left), dfs(node.Right)
        lv, rv := 0, 0
        if node.Val == left[0] {
            lv += left[1]
        }
        if node.Val == right[0] {
            rv += right[1]
        }
        return []int{node.Val, max(lv, rv) + 1, max(lv + rv + 1, left[2], right[2])}
    }

    ans := dfs(root)
    return max(0, max(ans[1], ans[2]) - 1)
}

func max(vals ...int) int {
    ans := vals[0]
    for _, v := range vals {
        if v > ans {
            ans = v
        }
    }
    return ans
}
```