# [Python/Java/TypeScript/Go] BFS

> slug: pythonjavatypescriptgo-by-himymben-s7l6
> date: 2022-06-21
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Find Bottom Left Tree Value (find-bottom-left-tree-value)
> url: https://leetcode.cn/problems/find-bottom-left-tree-value/solutions/OWzKaj/pythonjavatypescriptgo-by-himymben-s7l6/

---
### 解题思路
用BFS按层遍历，答案是最后一层的第一个节点的值

### 代码

```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue, ans = Deque([root]), None
        while queue:
            ans = queue[0].val
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans
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
    public int findBottomLeftValue(TreeNode root) {
        Deque<TreeNode> queue = new ArrayDeque<>();
        queue.addLast(root);
        int ans = 0;
        while (!queue.isEmpty()) {
            ans = queue.peekFirst().val;
            for (int i = 0, n = queue.size(); i < n; i++) {
                TreeNode node = queue.removeFirst();
                if (node.left != null) {
                    queue.addLast(node.left);
                }
                if (node.right != null) {
                    queue.addLast(node.right);
                }
            }
        }
        return ans;
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

function findBottomLeftValue(root: TreeNode | null): number {
    let queue = [root], ans = 0
    while (queue.length > 0) {
        ans = queue[0].val
        const nxt = new Array<TreeNode>()
        for (const node of queue) {
            if (node.left != null) {
                nxt.push(node.left)
            }
            if (node.right != null) {
                nxt.push(node.right)
            }
        }
        queue = nxt
    }
    return ans
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
func findBottomLeftValue(root *TreeNode) (ans int) {
    queue := []*TreeNode{root}
    for len(queue) > 0 {
        ans = queue[0].Val
        for i, n := 0, len(queue); i < n; i++ {
            node := queue[0]
            queue = queue[1:]
            if node.Left != nil {
                queue = append(queue, node.Left)
            }
            if node.Right != nil {
                queue = append(queue, node.Right)
            }
        }
    }
    return
}
```