# [Python/Java] An unusual idea without building a graph

> Author: Benhao
> Date: 2021-07-28
> Upvotes: 5
> Tags: Java, Python, Python3

---

### Approach
> The path from any node to root must intersect the path from root to target at some node, their common ancestor.
The distance between them is the sum of the distance from this node to their common ancestor and the distance from target to that ancestor.
Find all nodes for which this sum is k.

Specifically, use DFS to find the path from root to target, which gives target's distance to each ancestor on that path.
When searching for answer nodes, assume an ancestor is their common ancestor with target; the required distance from an answer node to that ancestor is then fixed. To handle a common ancestor closer to target, reset the current distance whenever another ancestor of target is encountered.

(Additional pruning: if neither child subtree contains any node on the root-to-target path and dis is already negative, no later node can be at distance k.)

### Code
```python3 []
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:
            return [target.val]
        elif k > 501:
            return []

        def dfs1(node, path):
            if node == target:
                return path + [node]
            if not node:
                return []
            left = dfs1(node.left, path+[node])
            if left:
                return left
            return dfs1(node.right, path+[node])
        
        dists = dfs1(root, [])
        parents_distance = dict()
        n = len(dists) - 1
        for i, node in enumerate(dists):
            parents_distance[node] = n - i
    
        ans = []

        def dfs2(node, parent, dis):
            if not node:
                return
            if node in parents_distance:
                parent = node
                dis = k - parents_distance[node]
            if not dis:
                ans.append(node.val)
            dfs2(node.left, parent, dis-1)
            dfs2(node.right, parent, dis-1)

        dfs2(root, None, k)
        return ans 
```
```java []
class Solution {
    ArrayList<Integer> ans;
    HashMap<TreeNode, Integer> map;
    int k_;

    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        ans = new ArrayList<>();
        map = new HashMap<>();
        k_ = k;
        ArrayList<TreeNode> path = dfs1(root, target);
        for(int i=0;i<path.size();i++)
            map.put(path.get(i), i);
        dfs2(root, k);
        return ans;
    }

    public ArrayList<TreeNode> dfs1(TreeNode node, TreeNode target){
        if(node == null)
            return null;
        if(node==target){
            ArrayList<TreeNode> res = new ArrayList<>();
            res.add(node);
            return res;
        }
        ArrayList<TreeNode> left, right;
        left = dfs1(node.left, target);
        if(left != null){
            left.add(node);
            return left;
        }
        right = dfs1(node.right, target);
        if(right != null){
            right.add(node);
            return right;
        }
        return null;
    }

    public void dfs2(TreeNode node, int dis){
        if(node == null)
            return;
        if(map.containsKey(node)){
            dis = k_ - map.get(node);
        }
        if(dis==0)
            ans.add(node.val);
        dfs2(node.left, --dis);
        dfs2(node.right, dis);
    }
}
```

Pruned version: runtime 99%
```python3 []
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:
            return [target.val]
        elif k > 501:
            return []

        def dfs1(node):
            if not node:
                return []
            if node == target:
                return [node]
            left = dfs1(node.left)
            if left:
                left.append(node)
                return left
            right = dfs1(node.right)
            if right:
                right.append(node)
            return right

        dists = dfs1(root)
        parents_distance = dict()
        for i, node in enumerate(dists):
            parents_distance[node] = i

        ans = []

        def dfs2(node, dis):
            if not node:
                return
            if node in parents_distance:
                dis = k - parents_distance[node]
            if dis < 0 and not (
                    (node.left and node.left in parents_distance) or (node.right and node.right in parents_distance)):
                return
            if not dis:
                ans.append(node.val)
            dfs2(node.left, dis - 1)
            dfs2(node.right, dis - 1)

        dfs2(root, k)
        return ans
```
```java []
class Solution {
    ArrayList<Integer> ans;
    HashMap<TreeNode, Integer> map;
    int k_;

    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        ans = new ArrayList<>();
        map = new HashMap<>();
        k_ = k;
        ArrayList<TreeNode> path = dfs1(root, target);
        for(int i=0;i<path.size();i++)
            map.put(path.get(i), i);
        dfs2(root, k);
        return ans;
    }

    public ArrayList<TreeNode> dfs1(TreeNode node, TreeNode target){
        if(node == null)
            return null;
        if(node==target){
            ArrayList<TreeNode> res = new ArrayList<>();
            res.add(node);
            return res;
        }
        ArrayList<TreeNode> left, right;
        left = dfs1(node.left, target);
        if(left != null){
            left.add(node);
            return left;
        }
        right = dfs1(node.right, target);
        if(right != null){
            right.add(node);
            return right;
        }
        return null;
    }

    public void dfs2(TreeNode node, int dis){
        if(node == null)
            return;
        if(map.containsKey(node)){
            dis = k_ - map.get(node);
        }
        if(dis<0 && !(node.left!=null && map.containsKey(node.left)) && !(node.right!=null && map.containsKey(node.right)))
            return;
        if(dis==0)
            ans.add(node.val);
        dfs2(node.left, --dis);
        dfs2(node.right, dis);
    }
}
```
