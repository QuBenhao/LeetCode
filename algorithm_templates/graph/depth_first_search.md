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

## Three-state visited discipline

The `visited` set above is enough while the traversal only needs reachability. It is **not** enough once each node's answer is a property of its whole component, merged from the neighbours' answers: then "already finished" and "still on the stack" must be told apart, otherwise two adjacent nodes of the same component call each other forever.

```text
UNVISITED    not entered yet
IN_PROGRESS  entered, answer still unknown (on the recursion stack)
DONE         every neighbour processed, answer final
```

Rules:

1. Mark `IN_PROGRESS` on entry, **before** recursing into the neighbours.
2. Meeting an `IN_PROGRESS` node means "the answer is not known yet": return the **identity element of the merge operator** — `True` for AND (all neighbours must hold), `False` for OR, `0` for a sum, `+inf` / `-inf` for a min / max. Returning a *decided* value here is the silent bug.
3. Store the result only when the node becomes `DONE`.

In an undirected graph a node that is `IN_PROGRESS` when you touch it is always an ancestor on the current path (there are no cross edges), and its own frame folds in whatever your subtree would have contributed. That is why the neutral value is safe.

Why `False` is wrong for an AND merge — take a closed 2x2 island:

```text
1 1 1 1
1 0 0 1
1 1 1 1
```

Starting at `(1,1)`, the neighbour `(1,2)` touches the `IN_PROGRESS` ancestor `(1,1)`. Returning `False` there ("assume not closed") turns `(1,2)` into `False`, and the whole island is reported as touching the border: answer 0 instead of 1.

### Template (1254. Number of Closed Islands, AND merge)

```python
def closedIsland(grid):
    m, n = len(grid), len(grid[0])
    UNVISITED, IN_PROGRESS, DONE = 0, 1, 2
    state = [[UNVISITED] * n for _ in range(m)]

    def dfs(i, j):
        if not (0 <= i < m and 0 <= j < n):
            return False                     # left the grid: the component touches the border
        if grid[i][j] == 1 or state[i][j] == DONE:
            return True                      # water / finished: identity of AND
        if state[i][j] == IN_PROGRESS:
            return True                      # on the stack: unknown, contributes identity
        state[i][j] = IN_PROGRESS
        ok = True
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ok &= dfs(i + di, j + dj)        # deliberately no short-circuit
        state[i][j] = DONE
        return ok

    return sum(dfs(i, j) for i in range(m) for j in range(n)
               if grid[i][j] == 0 and state[i][j] == UNVISITED)
```

Two follow-ups worth remembering:

- Write `ok &= dfs(...)`, not `ok and dfs(...)`: a short-circuit stops the traversal halfway through the component, leaving the rest `UNVISITED` so the outer loop counts the same component again.
- Every node of one component ends up with the same `DONE` value, so a per-node value cache is redundant; a plain `visited` set is enough. The third state only matters for the value a frame returns while it is still on the stack.

The same three states are the white / gray / black colouring of cycle detection: gray is `IN_PROGRESS`, and an edge into a gray node is a back edge, i.e. a cycle.

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
