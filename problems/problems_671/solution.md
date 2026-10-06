# [Python/Java] Recursion, iteration, and optimal recursion using the problem's constraints

> Author: Benhao
> Date: 2021-07-27
> Upvotes: 15
> Tags: Java, Python, Python3

---

### Approach
Have each recursive call return the two smallest values in the subtree. Use inf when a child is absent.
For an iterative solution, maintain the two smallest values.

The final code uses the problem's special property for the optimal recursive approach.

### Code
Ordinary recursion returning the two smallest values for each node
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

Iteration (BFS)
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

**The following recursion fully uses the property that each node's value is the minimum of its two children's values.**
```python3 []
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        # A second-smallest value cannot exist
        if not root or not root.left:
            return -1
        # We know root.val is the minimum, so
        # The second-smallest value is either in the smaller child's subtree or at the larger child
        left = root.left.val if root.left.val != root.val else self.findSecondMinimumValue(root.left)
        right = root.right.val if root.right.val != root.val else self.findSecondMinimumValue(root.right)
        return min(left, right) if left != -1 and right != -1 else max(left, right)
```
```java []
class Solution {
    public int findSecondMinimumValue(TreeNode root) {
        // A node whose subtree cannot contain a second-smallest value
        if(root == null || root.left == null)
            return -1;
        // Find the smallest value in either subtree that differs from the current node's value
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
