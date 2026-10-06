# [Python/Java] Recursive prefix sums 

> Author: Benhao
> Date: 2021-09-27
> Upvotes: 14
> Tags: Java, Python, Python3

---

### Approach
We need paths from any node to any descendant whose sum equals the target. Record prefix sums along the current path, then search for matching differences to count valid paths.

The left and right branches must not affect each other during recursion, so either copy the list or backtrack.
Backtracking is clearly better because copying is expensive.
Count occurrences of each prefix sum so that updating the answer no longer requires scanning the path.

### Code

```python3
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node, presum):
            if not node:
                return 0
            cur = presum[-1] + node.val
            # Number of paths ending at node with sum targetSum
            ans = sum(cur - p == targetSum for p in presum)
            presum.append(cur)
            return ans + dfs(node.left, list(presum)) + dfs(node.right, presum)
        
        return dfs(root, [0])
```

```Python3 []
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node, cnts, cursum):
            if not node:
                return 0
            cursum += node.val
            ans = cnts[cursum - targetSum]
            cnts[cursum] += 1
            if node.left:
                ans += dfs(node.left, cnts, cursum)
            if node.right:
                ans += dfs(node.right, cnts, cursum)
            cnts[cursum] -= 1
            return ans
        return dfs(root, Counter([0]), 0)
```
```Java []
class Solution {
    int target;
    public int pathSum(TreeNode root, int targetSum) {
        target = targetSum;
        Map<Integer, Integer> cnts = new HashMap<>();
        cnts.put(0, 1);
        return dfs(root,cnts,0);
    }

    public int dfs(TreeNode node, Map<Integer, Integer> cnts, int sum){
        if(node == null)
            return 0;
        sum += node.val;
        int ans = cnts.getOrDefault(sum - target, 0);
        cnts.put(sum, cnts.getOrDefault(sum, 0) + 1);
        if(node.left != null)
            ans += dfs(node.left, cnts, sum);
        if(node.right != null)
            ans += dfs(node.right, cnts, sum);
        cnts.put(sum, cnts.get(sum) - 1);
        return ans;
    }
}
```
