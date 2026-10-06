# [Python/Go] Maintain intervals (stronger test data would time out)

> slug: python-by-himymben-juh9
> date: 2022-04-16
> tags: Go, Python, Python3
> question: 二叉搜索树染色 (QO5KpG)
> url: https://leetcode.cn/problems/QO5KpG/solutions/qwD18A/python-by-himymben-juh9/

---
### Approach

For interval overwrites, the last update always takes effect. Process updates in reverse and remove intervals that have already been handled.
Convert the tree to an array and use binary search to map values to compact indices.
Maintain a sorted list by brute force.

(A faster approach uses union-find or a segment tree; add it later.)

### Code

```python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def getNumber(self, root: Optional[TreeNode], ops: List[List[int]]) -> int:
        def dfs(node):
            if node:
                yield from dfs(node.left)
                yield node.val
                yield from dfs(node.right)

        ans = 0        
        nums = [num for num in dfs(root)]
        for tp, x, y in ops[::-1]:
            ix, iy = bisect_left(nums, x), bisect_right(nums, y) - 1
            if ix <= iy:
                if tp:
                    ans += iy - ix + 1
                nums = nums[:ix] + nums[iy + 1:]
        return ans
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
func getNumber(root *TreeNode, ops [][]int) (ans int) {
    nums := []int{}

    var dfs func(node *TreeNode)
    dfs = func(node * TreeNode) {
        if node != nil {
            dfs(node.Left)
            nums = append(nums, node.Val)
            dfs(node.Right)
        }
    }

    dfs(root)
    for i := len(ops) - 1; i >= 0; i-- {
        ix, iy := bisectLeft(nums, ops[i][1]), bisectRight(nums, ops[i][2]) - 1
        if ix <= iy {
            if ops[i][0] == 1 {
                ans += iy - ix + 1
            }
            tmp := nums[iy + 1:]
            nums = nums[:ix]
            nums = append(nums, tmp...)
        }
    }
    return
}

func bisectLeft(nums []int, target int) int {
    l, r := 0, len(nums)
    for l < r {
        mid := (l + r) >> 1
        if nums[mid] >= target {
            r = mid
        } else {
            l = mid + 1
        }
    }
    return l
}

func bisectRight(nums []int, target int) int {
    l, r := 0, len(nums)
    for l < r {
        mid := (l + r) >> 1
        if nums[mid] > target {
            r = mid
        } else {
            l = mid + 1
        }
    }
    return l
}
```
