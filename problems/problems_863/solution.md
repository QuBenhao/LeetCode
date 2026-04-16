# [Python/Java] 奇思妙想(不建图)

> Author: Benhao
> Date: 2021-07-28
> Upvotes: 5
> Tags: Java, Python, Python3

---

### 解题思路
> 任意一个节点到root的路径 都必然和 root到target的路径 相交于某个节点(共同父节点)。
那么他们之间的距离就是 这个节点到这个共同父节点 + target到这个共同父节点 的距离之和。
求出所有和为k的即可。

具体来说，我们深度搜索找到root到target的路径，那么target到这些父节点的距离我们就都知道了。
在搜索答案的节点时，我们假设某个父节点作为共同父节点，那么答案的节点到这个父节点的距离也就固定了。在处理共同父节点要更靠近target的情况时，我们遇到是target的父节点，重新给当前距离赋值即可。

(可以额外剪枝，如果node的左右都没有root到target的任意路径节点了且dis已经小于0了，那么后面不可能存在距离为k的节点了)。

### 代码
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

剪枝版本时间 99%
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
