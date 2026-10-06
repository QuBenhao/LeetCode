# BFS

- Core ideas

1. **Queue**: Use a first-in, first-out queue to manage nodes awaiting a visit.
2. **Expand by level**: Process nodes level by level so that the shortest path is found first.
3. **Avoid repeated visits**: Track visited nodes, for example with a hash table or array of flags.

## Basic structure: level-order traversal of a tree or graph

```python
from collections import deque


def process(node):
    pass


def get_neighbors(node):
    return []


def bfs(start_node):
    queue = deque([start_node])  # Initialize the queue
    visited = set()  # Track visited nodes, which may be needed for a graph
    visited.add(start_node)  # Mark the starting node

    while queue:
        level_size = len(queue)  # Number of nodes at this level, needed for level-order traversal
        for _ in range(level_size):
            node = queue.popleft()
            # Process the current node, for example by visiting it or checking for the target
            process(node)
            # Iterate over adjacent nodes as defined by the problem
            for neighbor in get_neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    return
```

## Example: binary tree level-order traversal

```python
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


# Test
_root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(level_order(_root))  # Output: [[3], [9, 20], [15, 7]]
```

## Example: shortest path in a grid (0 is walkable, 1 is blocked)

```python
from collections import deque


def shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, down, left, right
    queue = deque([(start[0], start[1], 0)])  # (x, y, steps)
    visited = set()
    visited.add((start[0], start[1]))

    while queue:
        x, y, steps = queue.popleft()
        if (x, y) == end:
            return steps
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))
    return -1  # Unreachable


# Test
_grid = [
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0]
]
print(shortest_path(_grid, (0, 0), (3, 3)))  # Output: 6
```

## Basic structure: queue implementation

```go
package main

import (
    "container/list"
    "fmt"
)

// Tree node definition
type TreeNode struct {
    Val   int
    Left  *TreeNode
    Right *TreeNode
}

// Level-order traversal example
func levelOrder(root *TreeNode) [][]int {
    result := [][]int{}
    if root == nil {
        return result
    }
    queue := list.New()
    queue.PushBack(root)
    
    for queue.Len() > 0 {
        levelSize := queue.Len()
        level := make([]int, 0, levelSize)
        for i := 0; i < levelSize; i++ {
            node := queue.Remove(queue.Front()).(*TreeNode)
            level = append(level, node.Val)
            if node.Left != nil {
                queue.PushBack(node.Left)
            }
            if node.Right != nil {
                queue.PushBack(node.Right)
            }
        }
        result = append(result, level)
    }
    return result
}

// Test
func main() {
    root := &TreeNode{3, 
        &TreeNode{9, nil, nil}, 
        &TreeNode{20, 
            &TreeNode{15, nil, nil}, 
            &TreeNode{7, nil, nil},
        },
    }
    fmt.Println(levelOrder(root)) // Output: [[3] [9 20] [15 7]]
}
```

## Example: shortest path in a grid

```go
type Point struct {
    x, y, steps int
}

func shortestPath(grid [][]int, start, end [2]int) int {
    rows, cols := len(grid), len(grid[0])
    directions := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
    queue := list.New()
    visited := make(map[[2]int]bool)
    
    startX, startY := start[0], start[1]
    queue.PushBack(Point{startX, startY, 0})
    visited[[2]int{startX, startY}] = true
    
    for queue.Len() > 0 {
        front := queue.Front()
        queue.Remove(front)
        p := front.Value.(Point)
        if p.x == end[0] && p.y == end[1] {
            return p.steps
        }
        for _, dir := range directions {
            nx, ny := p.x + dir[0], p.y + dir[1]
            if nx >= 0 && nx < rows && ny >= 0 && ny < cols {
                if grid[nx][ny] == 0 && !visited[[2]int{nx, ny}] {
                    visited[[2]int{nx, ny}] = true
                    queue.PushBack(Point{nx, ny, p.steps + 1})
                }
            }
        }
    }
    return -1
}

// Test
func main() {
    grid := [][]int{
        {0,0,1,0},
        {0,0,0,0},
        {1,1,0,1},
        {0,0,0,0},
    }
    fmt.Println(shortestPath(grid, [2]int{0,0}, [2]int{3,3})) // Output: 6
}
```

## Key points about BFS

| Property | Description |
|-----------|------------------------------------------|
| **Time complexity** | O(N), where N is the number of nodes; each node is visited once. |
| **Space complexity** | O(N); in the worst case, the queue stores all nodes. |
| **Use cases** | Shortest paths in unweighted graphs, level-order traversal, topological sorting, and connected components. |
| **Checks** | 1. Mark visited nodes; 2. Handle empty input; 3. Initialize the queue correctly; 4. Check bounds. |

Adapt the **node definition**, **neighbor lookup**, and **termination condition** to the specific problem.
