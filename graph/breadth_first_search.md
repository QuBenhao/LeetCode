# BFS

- 核心思想

1. **队列结构**：用队列（先进先出）管理待访问的节点。
2. **逐层扩展**：按层处理节点，保证最先找到最短路径。
3. **避免重复访问**：记录已访问的节点（如哈希表、数组标记）。

## 基本结构（树/图的层序遍历）

```python
from collections import deque


def process(node):
    pass


def get_neighbors(node):
    return []


def bfs(start_node):
    queue = deque([start_node])  # 初始化队列
    visited = set()  # 记录已访问节点（图可能需要）
    visited.add(start_node)  # 标记初始节点

    while queue:
        level_size = len(queue)  # 当前层的节点数（层序遍历需要）
        for _ in range(level_size):
            node = queue.popleft()
            # 处理当前节点（如访问、判断目标等）
            process(node)
            # 遍历相邻节点（根据问题定义）
            for neighbor in get_neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    return
```

## 示例：二叉树层序遍历

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


# 测试
_root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(level_order(_root))  # 输出 [[3], [9, 20], [15, 7]]
```

## 示例：网格最短路径（0 可走，1 障碍）

```python
from collections import deque


def shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右
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
    return -1  # 不可达


# 测试
_grid = [
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0]
]
print(shortest_path(_grid, (0, 0), (3, 3)))  # 输出 6
```

## 基本结构（队列实现）

```go
package main

import (
    "container/list"
    "fmt"
)

// 树节点定义
type TreeNode struct {
    Val   int
    Left  *TreeNode
    Right *TreeNode
}

// 层序遍历示例
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

// 测试
func main() {
    root := &TreeNode{3, 
        &TreeNode{9, nil, nil}, 
        &TreeNode{20, 
            &TreeNode{15, nil, nil}, 
            &TreeNode{7, nil, nil},
        },
    }
    fmt.Println(levelOrder(root)) // 输出 [[3] [9 20] [15 7]]
}
```

## 示例：网格最短路径

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

// 测试
func main() {
    grid := [][]int{
        {0,0,1,0},
        {0,0,0,0},
        {1,1,0,1},
        {0,0,0,0},
    }
    fmt.Println(shortestPath(grid, [2]int{0,0}, [2]int{3,3})) // 输出 6
}
```

## BFS 关键点

| 特性        | 说明                                       |
|-----------|------------------------------------------|
| **时间复杂度** | O(N)，N 为节点数（每个节点访问一次）                    |
| **空间复杂度** | O(N)，最坏情况队列存储所有节点                        |
| **适用场景**  | 最短路径（无权图）、层序遍历、拓扑排序、连通块问题                |
| **注意事项**  | 1. 确保标记已访问节点；2. 处理空输入；3. 队列初始化正确；4. 边界检查 |

根据具体问题，调整 **节点定义**、**邻居获取方式** 和 **终止条件** 即可适配不同场景。
