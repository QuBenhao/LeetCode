# [Python/Java/TypeScript/Go] BFS

> slug: pythonjavatypescriptgo-bfs-by-himymben-6jcd
> date: 2022-06-23
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Find Largest Value in Each Tree Row (find-largest-value-in-each-tree-row)
> url: https://leetcode.cn/problems/find-largest-value-in-each-tree-row/solutions/Pmo5si/pythonjavatypescriptgo-bfs-by-himymben-6jcd/

---
### 解题思路
BFS层序遍历统计每层最大值即可

### 代码

```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue, ans = Deque([root]), []
        while queue:
            cur = -inf
            for _ in range(len(queue)):
                node = queue.popleft()
                cur = max(cur, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(cur)
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
    public List<Integer> largestValues(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        if (root != null) {
            Deque<TreeNode> queue = new ArrayDeque<>();
            queue.addLast(root);
            while(!queue.isEmpty()) {
                int cur = Integer.MIN_VALUE;
                for (int i = 0, n = queue.size(); i < n; i++) {
                    TreeNode node = queue.pollFirst();
                    cur = Math.max(cur, node.val);
                    if (node.left != null) {
                        queue.addLast(node.left);
                    }
                    if (node.right != null) {
                        queue.addLast(node.right);
                    }
                }
                ans.add(cur);
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

function largestValues(root: TreeNode | null): number[] {
    const ans = new Array<number>()
    if (root != null) {
        let queue = [root]
        while (queue.length > 0) {
            const nxt = new Array<TreeNode>()
            let cur = queue[0].val
            for (const node of queue) {
                cur = Math.max(cur, node.val)
                if (node.left != null) {
                    nxt.push(node.left)
                }
                if (node.right != null) {
                    nxt.push(node.right)
                }
            }
            queue = nxt
            ans.push(cur)
        }
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
func largestValues(root *TreeNode) (ans []int) {
    if root != nil {
        queue := []*TreeNode{root}
        for len(queue) > 0 {
            cur := queue[0].Val
            for i, n := 0, len(queue); i < n; i++ {
                node := queue[0]
                queue = queue[1:]
                if node.Val > cur {
                    cur = node.Val
                }
                if node.Left != nil {
                    queue = append(queue, node.Left)
                }
                if node.Right != nil {
                    queue = append(queue, node.Right)
                }
            }
            ans = append(ans, cur)
        }
    }
    return
}
```