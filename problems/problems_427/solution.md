# [Python/Java/JavaScript/Go] 二维前缀和

> Author: Benhao
> Date: 2022-04-28
> Upvotes: 47
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
本题需要递归枚举正方形，直到正方形全是1或全是0为止。
否则就切割成四个小正方形继续递归。

判断全1或全0可以很容易想到，二维前缀和的结果是正方形的大小或0。

### 代码

```Python3 []
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        m, n = len(grid), len(grid[0])
        presum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                presum[i + 1][j + 1] += presum[i + 1][j] + presum[i][j + 1] - presum[i][j] + grid[i][j]
        
        def dfs(x0, y0, x1, y1):
            if not (diff := presum[x1][y1] - presum[x1][y0] - presum[x0][y1] + presum[x0][y0]):
                return Node(False, True, None, None, None, None)
            elif diff == (x1 - x0) * (y1 - y0):
                return Node(True, True, None, None, None, None)
            else:
                # 这里填True、False都行
                return Node(True, False, dfs(x0, y0, hx:=(x0 + x1) // 2, hy:=(y0 + y1) // 2),
                                         dfs(x0, hy, hx, y1),
                                         dfs(hx, y0, x1, hy),
                                         dfs(hx, hy, x1, y1))
        
        return dfs(0, 0, m, n)
```
```Java []
/*
// Definition for a QuadTree node.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;

    
    public Node() {
        this.val = false;
        this.isLeaf = false;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }
    
    public Node(boolean val, boolean isLeaf) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }
    
    public Node(boolean val, boolean isLeaf, Node topLeft, Node topRight, Node bottomLeft, Node bottomRight) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = topLeft;
        this.topRight = topRight;
        this.bottomLeft = bottomLeft;
        this.bottomRight = bottomRight;
    }
};
*/

class Solution {
    private int[][] presum;
    public Node construct(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        presum = new int[m + 1][n + 1];
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
                presum[i + 1][j + 1] = presum[i + 1][j] + presum[i][j + 1] - presum[i][j] + grid[i][j];
        return dfs(0, 0, m, n);
    }

    private Node dfs(int x0, int y0, int x1, int y1) {
        int diff = presum[x1][y1] - presum[x1][y0] - presum[x0][y1] + presum[x0][y0];
        if(diff == 0)
            return new Node(false, true, null, null, null, null);
        if(diff == (x1 - x0) * (y1 - y0))
            return new Node(true, true, null, null, null, null);
        int hx = (x0 + x1) / 2, hy = (y0 + y1) / 2;
        return new Node(true, false,
                        dfs(x0, y0, hx, hy),
                        dfs(x0, hy, hx, y1),
                        dfs(hx, y0, x1, hy),
                        dfs(hx, hy, x1, y1));
    }
}
```
```JavaScript []
/**
 * // Definition for a QuadTree node.
 * function Node(val,isLeaf,topLeft,topRight,bottomLeft,bottomRight) {
 *    this.val = val;
 *    this.isLeaf = isLeaf;
 *    this.topLeft = topLeft;
 *    this.topRight = topRight;
 *    this.bottomLeft = bottomLeft;
 *    this.bottomRight = bottomRight;
 * };
 */

/**
 * @param {number[][]} grid
 * @return {Node}
 */
var construct = function(grid) {
    const m = grid.length, n = grid[0].length
    const presum = new Array(m + 1).fill(0).map(() => new Array(n + 1).fill(0));
    for(let i = 0; i < m; i++)
        for(let j = 0; j < n; j++)
            presum[i + 1][j + 1] = presum[i + 1][j] + presum[i][j + 1] - presum[i][j] + grid[i][j]
    dfs = function(x0, y0, x1, y1) {
        const diff = presum[x1][y1] - presum[x0][y1] - presum[x1][y0] + presum[x0][y0]
        if(diff == 0)
            return new Node(false, true, null, null, null, null)
        else if(diff == (x1 - x0) * (y1 - y0))
            return new Node(true, true, null, null, null, null)
        const hx = Math.floor((x0 + x1) / 2), hy = Math.floor((y0 + y1) / 2)
        return new Node(true, false,
                        dfs(x0, y0, hx, hy),
                        dfs(x0, hy, hx, y1),
                        dfs(hx, y0, x1, hy),
                        dfs(hx, hy, x1, y1))
    }
    return dfs(0, 0, m, n)
};
```
```Go []
/**
 * Definition for a QuadTree node.
 * type Node struct {
 *     Val bool
 *     IsLeaf bool
 *     TopLeft *Node
 *     TopRight *Node
 *     BottomLeft *Node
 *     BottomRight *Node
 * }
 */

func construct(grid [][]int) *Node {
    m, n := len(grid), len(grid[0])
    presum := make([][]int, m + 1)
    presum[0] = make([]int, n + 1)
    for i := 0; i < m; i++ {
        presum[i + 1] = make([]int, n + 1)
        for j := 0; j < n; j++ {
            presum[i + 1][j + 1] = presum[i + 1][j] + presum[i][j + 1] - presum[i][j] + grid[i][j]
        }
    }

    var dfs func(x0, y0, x1, y1 int) *Node
    dfs = func(x0, y0, x1, y1 int) * Node {
        if diff := presum[x1][y1] - presum[x1][y0] - presum[x0][y1] + presum[x0][y0]; diff == 0 {
            return &Node{false, true, nil, nil, nil, nil}
        } else if diff == (x1 - x0) * (y1 - y0) {
            return &Node{true, true, nil, nil, nil, nil}
        }
        hx, hy := (x0 + x1) / 2, (y0 + y1) / 2
        return &Node{true, false,
                    dfs(x0, y0, hx, hy),
                    dfs(x0, hy, hx, y1),
                    dfs(hx, y0, x1, hy),
                    dfs(hx, hy, x1, y1)}
    }

    return dfs(0, 0, m, n)
}
```