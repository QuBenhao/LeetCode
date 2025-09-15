# DFS

```python
def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)
    # 处理当前节点
    for neighbor in node.neighbors:
        dfs(neighbor, visited)
```

```go
func dfs(node *GraphNode, visited map[*GraphNode]bool) {
    if visited[node] {
        return
    }
    visited[node] = true
    // 处理当前节点
    for _, neighbor := range node.neighbors {
        dfs(neighbor, visited)
    }
}
```

## DFS时间戳

DFS时间戳是在深度优先搜索(DFS)过程中为每个节点记录的两个关键时间点：**发现时间(d_time)** 和**完成时间(f_time)**。这种技术广泛应用于树和图的各种算法中。

### 核心概念

1. **发现时间(d_time)**：节点第一次被访问的时间点
2. **完成时间(f_time)**：节点所有邻接节点都被访问完毕的时间点
3. **时间戳区间**：每个节点都有一个时间区间 `[d_time, f_time]`，该区间包含了其所有后代节点的时间区间

### 关键性质

- **祖先-后代关系**：如果节点u是节点v的祖先，则：
  ```
  d_time[u] < d_time[v] < f_time[v] < f_time[u]
  ```
- **无重叠关系**：如果两个节点的时间区间互不重叠，则它们之间没有祖先-后代关系
- **子树包含**：节点u的子树中所有节点的时间戳都在`[d_time[u], f_time[u]]`范围内

### 实现代码

```python
class TreeNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []

def dfs_timestamps(root):
    """为树中每个节点计算DFS时间戳"""
    timestamps = {}  # 存储每个节点的时间戳 (d_time, f_time)
    time = 0  # 全局时间计数器
    
    def dfs(node):
        nonlocal time
        if not node:
            return
        
        d_time = time  # 记录发现时间
        time += 1
        
        # 递归访问所有子节点
        for child in node.children:
            dfs(child)
        
        f_time = time  # 记录完成时间
        time += 1
        
        timestamps[node.val] = (d_time, f_time)
    
    dfs(root)
    return timestamps

# 构建示例树
#       1
#     / | \
#    2  3  4
#   / \     \
#  5   6     7
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node2 = TreeNode(2, [node5, node6])
node3 = TreeNode(3)
node4 = TreeNode(4, [node7])
root = TreeNode(1, [node2, node3, node4])

# 计算时间戳
timestamps = dfs_timestamps(root)

# 打印结果
print("节点 | 发现时间 | 完成时间")
print("-----------------------")
for node in sorted(timestamps.keys()):
    d, f = timestamps[node]
    print(f"  {node}  |    {d}      |    {f}")
```

### 输出示例

```
节点 | 发现时间 | 完成时间
-----------------------
  1  |    0      |    13
  2  |    1      |    8
  3  |    9      |    10
  4  |    11     |    12
  5  |    2      |    3
  6  |    4      |    5
  7  |    6      |    7
```

### 应用场景

1. **子树识别**：判断一个节点是否在另一个节点的子树中
2. **最近公共祖先(LCA)**：快速确定两个节点的最近公共祖先
3. **树链剖分**：优化树上路径查询
4. **拓扑排序**：对有向无环图进行排序
5. **环检测**：在图中检测环的存在
6. **强连通分量**：用于Tarjan算法等

### 使用示例：判断节点关系

```python
def is_ancestor(u, v, timestamps):
    """判断u是否是v的祖先"""
    d_u, f_u = timestamps[u]
    d_v, f_v = timestamps[v]
    return d_u < d_v and f_v < f_u

# 示例：判断节点2是否是节点5的祖先
print("节点2是节点5的祖先吗?", 
      is_ancestor(2, 5, timestamps))  # 输出: True

# 示例：判断节点1是否是节点7的祖先
print("节点1是节点7的祖先吗?", 
      is_ancestor(1, 7, timestamps))  # 输出: True

# 示例：判断节点3是否是节点6的祖先
print("节点3是节点6的祖先吗?", 
      is_ancestor(3, 6, timestamps))  # 输出: False
```
