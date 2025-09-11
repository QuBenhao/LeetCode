# 存图方式

## 邻接矩阵

这是一种使用**二维矩阵**来进行存图的方式

适用于边数较多的**稠密图**使用，当边数量接近点数量的平方，即$`m = n^2`$，可定义为稠密图

```python
# 稠密图适用（节点编号0~n-1）
n = 5
graph = [[0] * n for _ in range(n)]

# 添加边（带权重）
graph[0][1] = 3  # 0→1的边权重为3
graph[1][2] = 2  # 1→2的边权重为2
```

## 邻接表

```go
package main

// 稀疏图适用
type Graph struct {
    nodes int
    edges [][]int // edges[i]存储节点i的所有邻接节点
}

func NewGraph(n int) *Graph {
    return &Graph{
        nodes: n,
        edges: make([][]int, n),
    }
}

// 添加无向边
func (g *Graph) AddEdge(u, v int) {
    g.edges[u] = append(g.edges[u], v)
    g.edges[v] = append(g.edges[v], u)
}
```

## 类存图（带权重）

```python
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []  # 存储元组(node, weight)


# 构建示例
node0 = GraphNode(0)
node1 = GraphNode(1)
node0.neighbors.append((node1, 5))  # 0→1的边权重为5
```
