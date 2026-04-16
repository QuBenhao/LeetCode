# [Python/Java] 递归 or 迭代 以及 本题条件下的最优递归解法

> Author: Benhao
> Date: 2021-07-27
> Upvotes: 15
> Tags: Java, Python, Python3

---

### 解题思路
递归时返回每个节点返回该节点最小的两个值，如果没有子节点，加入inf。
迭代维护最小的两个值即可。

利用本题的题目条件的递归见最后一个代码(最优写法)。

### 代码
普通递归返回每个节点的最小的两个值
```python3
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res = self.dfs(root)
        return res[1] if res[1] != inf else -1
    
    def dfs(self, root):
        if not root.left:
            return root.val, inf
        l1, l2 = self.dfs(root.left)
        r1, r2 = self.dfs(root.right)
        return ans if len(ans:=sorted(set([l1, l2, r1, r2]))[:2]) == 2 else ans + [inf]
```

迭代 (BFS)
```python3 []
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        q = deque([root])
        ans = []
        while q:
            node = q.popleft()
            if -node.val not in ans:
                heapq.heappush(ans, -node.val)
                if len(ans) > 2:
                    heapq.heappop(ans)
            if node.left:
                q.append(node.left)
                q.append(node.right)
        return -ans[0] if len(ans) == 2 else -1

```
```java []
class Solution {
    public int findSecondMinimumValue(TreeNode root) {
        Deque<TreeNode> deque = new LinkedList();
        deque.addLast(root);
        HashSet<Integer> ans = new HashSet<>();
        while(deque.size() > 0){
            TreeNode node = deque.pollFirst();
            ans.add(node.val);
            if(node.left != null){
                deque.addLast(node.left);
                deque.addLast(node.right);
            }
        }
        if(ans.size() < 2)
            return -1;
        List<Integer> res = new ArrayList<>(ans);
        Collections.sort(res);
        return res.get(1);
    }
}
```

**但这样递归才能最大程度的利用每个节点都是它的两个子节点最小值的这一性质**
```python3 []
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        # 必然不存在第二小的值
        if not root or not root.left:
            return -1
        # 我们知道root.val是最小值，那么
        # 第二小的值存在于 更小的子节点那一边的子树的第二小的值 或 更大的子节点 之中
        left = root.left.val if root.left.val != root.val else self.findSecondMinimumValue(root.left)
        right = root.right.val if root.right.val != root.val else self.findSecondMinimumValue(root.right)
        return min(left, right) if left != -1 and right != -1 else max(left, right)
```
```java []
class Solution {
    public int findSecondMinimumValue(TreeNode root) {
        // 必然不存在第二小的值的节点
        if(root == null || root.left == null)
            return -1;
        // 第二小的值存在于左右子树不同于当前节点的最小值
        int left = root.val == root.left.val ? findSecondMinimumValue(root.left) : root.left.val;
        int right = root.val == root.right.val ? findSecondMinimumValue(root.right) : root.right.val;
        if(left == -1)
            return right;
        if(right == -1)
            return left;
        return Math.min(left, right);
    }
}
```
