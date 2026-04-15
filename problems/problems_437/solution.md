# [Python/Java] 递归前缀和 

> Author: Benhao
> Date: 2021-09-27
> Upvotes: 14
> Tags: Java, Python, Python3

---

### 解题思路
因为我们要讨论任意节点开始，到任意子节点的路径的和是否等于目标和，所以最好的办法就是记录这条路径的前缀和，然后遍历搜是否有相等的来统计个数即可。

在递归时，左右的要互不影响，要么复制一下list，要么回溯。
回溯显然更优，因为复制的代价很大。
我们可以统计和为某个值的数量，这样在统计答案时就不再需要遍历了。

### 代码

```python3
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node, presum):
            if not node:
                return 0
            cur = presum[-1] + node.val
            # 以node结尾，和为targetSum的个数
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