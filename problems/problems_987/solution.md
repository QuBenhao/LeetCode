# [Python/Java] 哈希表

> Author: Benhao
> Date: 2021-07-30
> Upvotes: 16
> Tags: Java, Python, Python3

---

### 解题思路
记录每一个列出现的所有数字(带行数)，按列排序，按行排序，按值排序即可。

### 代码
```python3 []
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        hashmap = defaultdict(list)
        def dfs(node, x, y):
            if not node:
                return
            hashmap[y].append((x,node.val))
            dfs(node.left, x+1, y-1)
            dfs(node.right,x+1, y+1)
        
        dfs(root, 0, 0)
        return [list(zip(*sorted(hashmap[i])))[1] for i in sorted(hashmap.keys())]
```
```Java []
class Solution {
    Map<Integer, Map<Integer, List<Integer>>> col2row2nodes = new HashMap<>();
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        dfs(root, 0, 0);
        List<Integer> colList = new ArrayList<>(col2row2nodes.keySet());
        Collections.sort(colList);
        for(int col: colList){
            Map<Integer, List<Integer>> row2nodes = col2row2nodes.get(col);
            List<Integer> rowList = new ArrayList<>(row2nodes.keySet()), cur = new ArrayList<>();
            Collections.sort(rowList);
            for(int row: rowList){
                List<Integer> nodes = row2nodes.get(row);
                Collections.sort(nodes);
                cur.addAll(nodes);
            }
            ans.add(cur);
        }
        return ans;
    }

    public void dfs(TreeNode root, int col, int row){
        if(root==null)
            return;
        Map<Integer, List<Integer>> row2nodes = col2row2nodes.getOrDefault(col, new HashMap<>());
        List<Integer> nodes = row2nodes.getOrDefault(row, new ArrayList<>());
        nodes.add(root.val);
        row2nodes.put(row, nodes);
        col2row2nodes.put(col, row2nodes);
        dfs(root.left, col-1, row+1);
        dfs(root.right, col+1, row+1);
    }
}
```
