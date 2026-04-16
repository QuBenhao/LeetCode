# [Python/Java/TypeScript/Go] DFS节点编号

> Author: Benhao
> Date: 2022-09-04
> Upvotes: 24
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
我们知道当两个树节点的左节点一致、右节点一致、根的值一致时，他们是重复的子树。
所以我们先对树的子节点进行递归，判断子节点是不是一致，后面再判断当前父节点是不是一致。
我们对每个独特的树节点进行哈希(根节点值、左节点编号、右节点编号)和编号(按出现顺序)，比如说第一个叶子节点为4，那么[4,null,null]为它的解构，0为它的编号。
这样它的父节点的左节点，就可以用编号0表示了。于是它的父节点2的解构就是[2,0,null]，1是它的编号。
也就是说每个节点左右节点均为编号，编号对比是否一致是很容易的。

### 代码

```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        memo, idx, ans = dict(), 0, []
        def dfs(node):
            left = right = None
            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)
            cur = (node.val, left, right)
            if cur in memo:
                if not memo[cur][1]:
                    ans.append(node)
                    memo[cur][1] += 1
                return memo[cur][0]
            else:
                nonlocal idx
                memo[cur] = [idx, 0]
                idx += 1
                return idx - 1
        
        dfs(root)
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
    private List<TreeNode> list;
    private int idx;
    private Map<Mark, Integer> map;
    private Set<Integer> set;

    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        map = new HashMap<>();
        set = new HashSet<>();
        list = new ArrayList<>();
        idx = 1;
        dfs(root);
        return list;
    }

    public int dfs(TreeNode node) {
        int left = 0, right = 0;
        if (node.left != null) {
            left = dfs(node.left);
        }
        if (node.right != null) {
            right = dfs(node.right);
        }
        Mark mark = new Mark(node.val, left, right);
        if (map.containsKey(mark)) {
            int cur = map.get(mark);
            if (!set.contains(cur)) {
                set.add(cur);
                list.add(node);
            }
            return cur;
        }  else {
            map.put(mark, idx++);
            return idx - 1;
        }
    }

    public static class Mark {
        public int nodeVal, leftIdx, rightIdx;

        public Mark(int nodeVal, int leftIdx, int rightIdx) {
            this.nodeVal = nodeVal;
            this.leftIdx = leftIdx;
            this.rightIdx = rightIdx;
        }

        @Override
        public boolean equals(Object other) {
            if (!(other instanceof Mark)) {
                return false;
            }
            Mark mark = (Mark) other;
            return nodeVal == mark.nodeVal && leftIdx == mark.leftIdx && rightIdx == mark.rightIdx;
        }

        @Override
        public int hashCode() {
            return (nodeVal + 200) * 100000000 + leftIdx * 10000 + rightIdx;
        }
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

function findDuplicateSubtrees(root: TreeNode | null): Array<TreeNode | null> {
    const hash = (val: number, left: number, right: number): number => {
        return (val + 200) * 100000000 + left * 10000 + right
    }, memo: Map<number, number> = new Map<number, number>(), explored: Set<number> = new Set<number>(), ans: Array<TreeNode> = new Array<TreeNode>()
    let idx: number = 1
    
    const dfs = (node: TreeNode): number => {
        let left: number = 0, right: number = 0
        if (node.left != null) {
            left = dfs(node.left)
        }
        if (node.right != null) {
            right = dfs(node.right)
        }
        const mark = hash(node.val, left, right)
        if (memo.has(mark)) {
            if (!explored.has(mark)) {
                explored.add(mark)
                ans.push(node)
            }
        } else {
            memo.set(mark, idx++)
        }
        return memo.get(mark)
    }
    dfs(root)
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
func findDuplicateSubtrees(root *TreeNode) []*TreeNode {
    memo, explored, ans, idx := map[int]int{}, map[int]bool{}, []*TreeNode{}, 1
    var dfs func(node *TreeNode) int
    dfs = func(node *TreeNode) int {
        left, right := 0, 0
        if node.Left != nil {
            left = dfs(node.Left)
        }
        if node.Right != nil {
            right = dfs(node.Right)
        }
        cur := hash(node.Val, left, right)
        if v, ok := memo[cur]; ok {
            if !explored[cur] {
                explored[cur] = true
                ans = append(ans, node)
            }
            return v
        } else {
            memo[cur] = idx
            idx++
            return idx - 1
        }
    }
    dfs(root)
    return ans
}

func hash (val, left, right int) int {
    return (val + 200) * 100000000 + left * 10000 + right
}
```