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

## 三态访问标记（visited 纪律）

上面那个 `visited` 集合只够应付「求可达性」。一旦每个节点的答案是**整个连通分量的属性**、并且要靠合并邻居的返回值算出来，就必须区分「已经算完」和「还在栈上」——否则同一分量内两个相邻节点会互相递归，直到爆栈。

```text
UNVISITED    还没进入
IN_PROGRESS  已进入，答案未知（在递归栈上）
DONE         邻居全部处理完，答案已定
```

三条规则：

1. 进入时立刻标 `IN_PROGRESS`，**在**递归邻居之前。
2. 遇到 `IN_PROGRESS` 的节点表示「答案还不知道」，此时要返回**合并运算的单位元**——AND 返回 `True`（全部成立），OR 返回 `False`，求和返回 `0`，取最值返回不影响合并的极值。这里返回一个「已定」的值就是那个不报错的 bug。
3. 只有在节点变成 `DONE` 时才落最终值。

无向图里你遇到的 `IN_PROGRESS` 节点一定是当前路径上的祖先（不存在横叉边），它自己的栈帧会把你这一支本该贡献的信息汇总进去，所以返回中性值是安全的。

为什么 AND 合并时返回 `False` 是错的——看这个被水完全包住的 2×2 岛：

```text
1 1 1 1
1 0 0 1
1 1 1 1
```

从 `(1,1)` 出发，邻居 `(1,2)` 会碰到还在 `IN_PROGRESS` 的祖先 `(1,1)`。若这里返回 `False`（「按不封闭算」），`(1,2)` 就被判成 `False`，整块会被误报成接触边界：答案 0 而不是 1。

### 模板（1254. 统计封闭岛屿的数目，AND 合并）

```python
def closedIsland(grid):
    m, n = len(grid), len(grid[0])
    UNVISITED, IN_PROGRESS, DONE = 0, 1, 2
    state = [[UNVISITED] * n for _ in range(m)]

    def dfs(i, j):
        if not (0 <= i < m and 0 <= j < n):
            return False                     # 越界：该分量接触边界
        if grid[i][j] == 1 or state[i][j] == DONE:
            return True                      # 水 / 已完成：AND 的单位元
        if state[i][j] == IN_PROGRESS:
            return True                      # 在栈上：答案未知，贡献单位元
        state[i][j] = IN_PROGRESS
        ok = True
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ok &= dfs(i + di, j + dj)        # 故意不短路
        state[i][j] = DONE
        return ok

    return sum(dfs(i, j) for i in range(m) for j in range(n)
               if grid[i][j] == 0 and state[i][j] == UNVISITED)
```

两个顺带要记住的点：

- 写 `ok &= dfs(...)` 而不是 `ok and dfs(...)`：短路会让遍历在半路停住，分量里剩下的格子还是 `UNVISITED`，主循环会把同一块再数一次。
- 同一个分量的所有节点最终值都一样，所以「逐节点存值」是冗余的，一个普通 `visited` 集合就够；第三态真正影响的是栈帧**返回时**给出的那个值。

同样的三态就是判环时的白 / 灰 / 黑染色：灰色即 `IN_PROGRESS`，指向灰点的边就是返祖边，也就是环。

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
