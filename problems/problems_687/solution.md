# [Python/Java/TypeScript/Go] DFS

> Author: Benhao
> Date: 2022-09-02
> Upvotes: 16
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### Approach
The Ja\va language option would not display, folks (it seems to be fixed now).
Here is a WA version first. I initially overlooked that a path connects any two nodes.
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
            Return the longest path and the length of the path ending at the root.
            """
            if not node:
                # Root value, path length ending at the root, longest path length
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
For maxima on trees, recursively obtain the children's results, combine them at the root, and return the result. This is similar to tree DP.
Maintain the path length ending at the root, which was the source of the initial error, and the maximum path joining both sides through the root.
A path connects two endpoints, so the value returned for the root cannot already join two branches. Return the longest path ending at the root so its parent can use it as one half of a longer path.

### Code

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
            Return the longest path and the length of the path ending at the root.
            """
            if not node:
                # Root value, longest path ending at the root without joining branches, longest overall path
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
