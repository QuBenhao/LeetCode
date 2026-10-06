# Graph representations

## Adjacency matrix

This representation stores a graph in a **two-dimensional matrix**.

It suits **dense graphs**, which have many edges. A graph is considered dense when the number of edges approaches the square of the number of nodes, that is, $`m = n^2`$.

```python
# Suitable for dense graphs with nodes numbered 0 to n-1
n = 5
graph = [[0] * n for _ in range(n)]

# Add weighted edges
graph[0][1] = 3  # Edge 0→1 has weight 3
graph[1][2] = 2  # Edge 1→2 has weight 2
```

## Adjacency list

```go
package main

// Suitable for sparse graphs
type Graph struct {
    nodes int
    edges [][]int // edges[i] stores all neighbors of node i
}

func NewGraph(n int) *Graph {
    return &Graph{
        nodes: n,
        edges: make([][]int, n),
    }
}

// Add an undirected edge
func (g *Graph) AddEdge(u, v int) {
    g.edges[u] = append(g.edges[u], v)
    g.edges[v] = append(g.edges[v], u)
}
```

## Class-based representation of a weighted graph

```python
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []  # Store (node, weight) tuples


# Construction example
node0 = GraphNode(0)
node1 = GraphNode(1)
node0.neighbors.append((node1, 5))  # Edge 0→1 has weight 5
```
