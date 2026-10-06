# DFS

```python
def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)
    # Process the current node
    for neighbor in node.neighbors:
        dfs(neighbor, visited)
```

```go
func dfs(node *GraphNode, visited map[*GraphNode]bool) {
    if visited[node] {
        return
    }
    visited[node] = true
    // Process the current node
    for _, neighbor := range node.neighbors {
        dfs(neighbor, visited)
    }
}
```

## DFS timestamps

DFS timestamps record two key moments for each node during depth-first search (DFS): its **discovery time (d_time)** and **finish time (f_time)**. This technique is widely used in tree and graph algorithms.

### Core concepts

1. **Discovery time (d_time)**: When the node is first visited
2. **Finish time (f_time)**: When all of the node's neighbors have been visited
3. **Timestamp interval**: Each node has an interval `[d_time, f_time]` that contains the intervals of all its descendants

### Key properties

- **Ancestor-descendant relationship**: If node u is an ancestor of node v, then:
  ```
  d_time[u] < d_time[v] < f_time[v] < f_time[u]
  ```
- **Disjoint intervals**: If two nodes have nonoverlapping intervals, neither is an ancestor of the other
- **Subtree containment**: The timestamps of every node in u's subtree lie within `[d_time[u], f_time[u]]`

### Implementation

```python
class TreeNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []

def dfs_timestamps(root):
    """Compute DFS timestamps for every node in the tree."""
    timestamps = {}  # Store each node's timestamps (d_time, f_time)
    time = 0  # Global time counter
    
    def dfs(node):
        nonlocal time
        if not node:
            return
        
        d_time = time  # Record the discovery time
        time += 1
        
        # Visit every child recursively
        for child in node.children:
            dfs(child)
        
        f_time = time  # Record the finish time
        time += 1
        
        timestamps[node.val] = (d_time, f_time)
    
    dfs(root)
    return timestamps

# Build the example tree
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

# Compute timestamps
timestamps = dfs_timestamps(root)

# Print the results
print("节点 | 发现时间 | 完成时间")
print("-----------------------")
for node in sorted(timestamps.keys()):
    d, f = timestamps[node]
    print(f"  {node}  |    {d}      |    {f}")
```

### Example output

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

### Applications

1. **Subtree membership**: Check whether one node belongs to another node's subtree
2. **Lowest common ancestor (LCA)**: Quickly find the lowest common ancestor of two nodes
3. **Heavy-light decomposition**: Optimize path queries on trees
4. **Topological sorting**: Order the nodes of a directed acyclic graph
5. **Cycle detection**: Detect cycles in a graph
6. **Strongly connected components**: Used in algorithms such as Tarjan's algorithm

### Usage example: checking node relationships

```python
def is_ancestor(u, v, timestamps):
    """Check whether u is an ancestor of v."""
    d_u, f_u = timestamps[u]
    d_v, f_v = timestamps[v]
    return d_u < d_v and f_v < f_u

# Example: check whether node 2 is an ancestor of node 5
print("节点2是节点5的祖先吗?", 
      is_ancestor(2, 5, timestamps))  # Output: True

# Example: check whether node 1 is an ancestor of node 7
print("节点1是节点7的祖先吗?", 
      is_ancestor(1, 7, timestamps))  # Output: True

# Example: check whether node 3 is an ancestor of node 6
print("节点3是节点6的祖先吗?", 
      is_ancestor(3, 6, timestamps))  # Output: False
```
