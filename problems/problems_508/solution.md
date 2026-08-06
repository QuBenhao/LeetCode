# [Python/Java/TypeScript/Go] 哈希表 + 递归

> slug: pythonjavatypescriptgo-di-gui-by-himymbe-9tds
> date: 2022-06-19
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Most Frequent Subtree Sum (most-frequent-subtree-sum)
> url: https://leetcode.cn/problems/most-frequent-subtree-sum/solutions/tEbAcB/pythonjavatypescriptgo-di-gui-by-himymbe-9tds/

---
### 解题思路
递归子树的和，根据子树和以及自身值，得到自己作为根的和，统计和的次数，返回自己的和给上层节点计算。

### 代码

```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        cnts = Counter()
        def dfs(node: TreeNode) -> int:
            if node:
                left, right = dfs(node.left), dfs(node.right)
                cnts[v := node.val + left + right] += 1
                return v
            return 0
        dfs(root)
        return [k for k, v in cnts.items() if v == most] if (most := max(cnts.values())) != inf else []
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
    private Map<Integer, Integer> map;

    public int[] findFrequentTreeSum(TreeNode root) {
        map = new HashMap<>();
        dfs(root);
        int mx = 0;
        final List<Integer> ans = new ArrayList<>();
        for(int k: map.keySet()) {
            int v = map.get(k);
            if (v > mx) {
                ans.clear();
                mx = v;
                ans.add(k);
            } else if (v == mx) {
                ans.add(k);
            }
        }
        int[] res = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) {
            res[i] = ans.get(i);
        }
        return res;
    }

    private int dfs(TreeNode node) {
        if (node != null) {
            int left = dfs(node.left), right = dfs(node.right);
            int cur = node.val + left + right;
            map.put(cur, map.getOrDefault(cur, 0) + 1);
            return cur;
        }
        return 0;
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

function findFrequentTreeSum(root: TreeNode | null): number[] {
    const cnts = new Map()
    const dfs = (node: TreeNode | null): number => {
        if (node != null) {
            const left = dfs(node.left), right = dfs(node.right)
            const cur = node.val + left + right
            if (cnts.has(cur)) {
                cnts.set(cur, cnts.get(cur) + 1)
            } else {
                cnts.set(cur, 1)
            }
            return cur
        }
        return 0
    }
    dfs(root)
    let ans = new Array(), mx = 0
    for (const [k, v] of cnts.entries()) {
        if (v > mx) {
            ans = [k]
            mx = v
        } else if (v == mx) {
            ans.push(k)
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
func findFrequentTreeSum(root *TreeNode) (ans []int) {
    cnts := map[int]int{}
    var dfs func(node *TreeNode) int
    dfs = func(node *TreeNode) int {
        if (node != nil) {
            left, right := dfs(node.Left), dfs(node.Right)
            cur := node.Val + left + right
            cnts[cur] += 1
            return cur
        }
        return 0
    }
    dfs(root)
    mx := 0
    for k, v := range cnts {
        if v > mx {
            ans = []int{k}
            mx = v
        } else if v == mx {
            ans = append(ans, k)
        }
    }
    return
}
```