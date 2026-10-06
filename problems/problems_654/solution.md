# [Python/Java/TypeScript/Go] Recursion && monotonic stack

> slug: python-by-himymben-1kn0
> date: 2022-08-20
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Maximum Binary Tree (maximum-binary-tree)
> url: https://leetcode.cn/problems/maximum-binary-tree/solutions/RP8eR8/python-by-himymben-1kn0/

---
### Approach
The maximum value in a sequence becomes the root. Recursively construct its left and right subtrees from the values on either side.

Repeatedly finding the maximum of each subsequence is expensive. A monotonic stack can optimize this by handling interval maxima.

### Code

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return TreeNode(mx, self.constructMaximumBinaryTree(nums[:idx]), self.constructMaximumBinaryTree(nums[idx + 1:])) if nums and (mx := max(nums)) != inf and (idx := nums.index(mx)) > -1 else None
```

```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for num in nums:
            cur = TreeNode(num)
            while stack and stack[-1].val < num:
                cur.left = stack.pop()
            if stack:
                stack[-1].right = cur
            stack.append(cur)
        return stack[0]
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
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        Deque<TreeNode> stack = new ArrayDeque<>();
        for (int num: nums) {
            TreeNode cur = new TreeNode(num);
            while (!stack.isEmpty() && stack.peekLast().val < num) {
                cur.left = stack.removeLast();
            }
            if (!stack.isEmpty()) {
                stack.peekLast().right = cur;
            }
            stack.addLast(cur);
        }
        return stack.peekFirst();
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

function constructMaximumBinaryTree(nums: number[]): TreeNode | null {
    const stack: Array<TreeNode> = new Array<TreeNode>()
    for (const num of nums) {
        const cur: TreeNode = new TreeNode(num)
        while (stack.length > 0 && stack[stack.length - 1].val < num) {
            cur.left = stack.pop()
        }
        if (stack.length > 0) {
            stack[stack.length - 1].right = cur
        }
        stack.push(cur)
    }
    return stack[0]
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
func constructMaximumBinaryTree(nums []int) *TreeNode {
    stack := []*TreeNode{}
    for _, num := range nums {
        cur := &TreeNode{num, nil, nil}
        for len(stack) > 0 && stack[len(stack) - 1].Val < num {
            cur.Left = stack[len(stack) - 1]
            stack = stack[:len(stack) - 1]
        }
        if len(stack) > 0 {
            stack[len(stack) - 1].Right = cur
        }
        stack = append(stack, cur)
    }
    return stack[0]
}
```
