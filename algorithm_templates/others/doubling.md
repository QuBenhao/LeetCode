# 倍增

倍增（Doubling）是一种**预处理数据并利用二进制思想优化查询效率**的算法技术。其核心思想是通过构建一个**跳转表**（如稀疏表，Sparse
Table），使得每次查询或操作的时间复杂度从线性降低到对数级别（如 $`O(\log n)`$。以下是其核心要点和应用场景：

## **倍增的核心原理**

1. **二进制分解**  
   将问题分解为多个**按指数递增的步长**（如 $`2^0, 2^1, 2^2, \dots`$）来处理。例如，跳转表中存储从每个位置出发，经过 $`2^k`$
   步后的结果。

2. **预处理跳转表**  
   构建一个二维数组 `dp[k][i]`，表示从位置 `i` 出发，跳转 $`2^k`$ 步后的目标位置或计算结果。例如：
    - `dp[0][i]` 表示跳转 1 步（$`2^0 = 1`$）后的结果。
    - `dp[k][i] = dp[k-1][ dp[k-1][i] ]`，即通过递归方式构建跳转表。

3. **快速查询**  
   将目标步长分解为二进制形式，按位累加跳转步长。例如，跳转 13 步（二进制 `1101`）时，分解为 $`8 + 4 + 1`$ 步，依次跳转 $
   `2^3, 2^2, 2^0`$ 步。

## **典型应用场景**

### 最近公共祖先

- **问题**：在树中快速找到两个节点的最近公共祖先。
- **倍增实现**：
    1. 预处理每个节点的 $`2^k`$ 级祖先（`up[k][u]`）。
    2. 先将两个节点调整到同一深度，再同时向上跳转，直到找到公共祖先。
- **时间复杂度**：预处理 $`O(n \log n)`$，查询 $`O(\log n)`$。
- **例**: [3553.包含给定路径的最小带权子树 II](problems/problems_3553/problem_zh.md)

```python
from typing import List


class TreeAncestor:
    def __init__(self, edges: List[List[int]]):
        n = len(edges) + 1
        m = n.bit_length()
        g = [[] for _ in range(n)]
        for x, y in edges:  # 节点编号从 0 开始
            g[x].append(y)
            g[y].append(x)

        depth = [0] * n
        pa = [[-1] * m for _ in range(n)]

        def dfs(x: int, fa: int) -> None:
            pa[x][0] = fa
            for y in g[x]:
                if y != fa:
                    depth[y] = depth[x] + 1
                    dfs(y, x)

        dfs(0, -1)

        for i in range(m - 1):
            for x in range(n):
                if (p := pa[x][i]) != -1:
                    pa[x][i + 1] = pa[p][i]
        self.depth = depth
        self.pa = pa

    def get_kth_ancestor(self, node: int, k: int) -> int:
        for i in range(k.bit_length()):
            if k >> i & 1:  # k 二进制从低到高第 i 位是 1
                node = self.pa[node][i]
        return node

    # 返回 x 和 y 的最近公共祖先（节点编号从 0 开始）
    def get_lca(self, x: int, y: int) -> int:
        if self.depth[x] > self.depth[y]:
            x, y = y, x
        # 使 y 和 x 在同一深度
        y = self.get_kth_ancestor(y, self.depth[y] - self.depth[x])
        if y == x:
            return x
        for i in range(len(self.pa[x]) - 1, -1, -1):
            px, py = self.pa[x][i], self.pa[y][i]
            if px != py:
                x, y = px, py  # 同时往上跳 2**i 步
        return self.pa[x][0]
```

```go
pacakge main

type TreeAncestor struct {
	n        int
	m        int
	depth    []int
	pa       [][]int
	distance []int
}

func Constructor(edges [][]int) TreeAncestor {
	n := len(edges) + 1
	graph := make(map[int][][]int, n)
	for _, edge := range edges {
		u, v, w := edge[0], edge[1], edge[2]
		graph[u] = append(graph[u], []int{v, w})
		graph[v] = append(graph[v], []int{u, w})
	}

	m := bits.Len(uint(n))
	depth := make([]int, n)
	pa := make([][]int, n)
	distance := make([]int, n)
	for i := range pa {
		pa[i] = make([]int, m)
	}

	var dfs func(node, parent int)
	dfs = func(node, parent int) {
		pa[node][0] = parent
		for _, child := range graph[node] {
			c, w := child[0], child[1]
			if c == parent {
				continue
			}
			depth[c] = depth[node] + 1
			distance[c] = distance[node] + w
			dfs(c, node)
		}
	}

	dfs(0, -1)
	for j := range m - 1 {
		for i := range n {
			if pa[i][j] != -1 {
				pa[i][j+1] = pa[pa[i][j]][j]
			} else {
				pa[i][j+1] = -1
			}
		}
	}

	return TreeAncestor{
		n:        n,
		m:        m,
		depth:    depth,
		pa:       pa,
		distance: distance,
	}
}

func (ta *TreeAncestor) GetKthAncestor(node, k int) int {
	for ; k > 0 && node != -1; k &= k - 1 {
		node = ta.pa[node][bits.TrailingZeros(uint(k))]
	}
	return node
}

func (ta *TreeAncestor) GetLCA(u, v int) int {
	if ta.depth[u] > ta.depth[v] {
		u, v = v, u
	}
	v = ta.GetKthAncestor(v, ta.depth[v]-ta.depth[u])
	if v == u {
		return u
	}
	for i := ta.m - 1; i >= 0; i-- {
		if ta.pa[u][i] != ta.pa[v][i] {
			u = ta.pa[u][i]
			v = ta.pa[v][i]
		}
	}
	return ta.pa[u][0]
}

func (ta *TreeAncestor) GetDistance(u, v int) int {
	lca := ta.GetLCA(u, v)
	return ta.distance[u] + ta.distance[v] - 2*ta.distance[lca]
}

func (t *TreeAncestor) FindDistance(x, d int) int {
	d = t.distance[x] - d
	for j := t.m - 1; j >= 0; j-- {
		if p := t.pa[x][j]; p != -1 && t.distance[p] >= d {
			x = p
		}
	}
	return x
}
```

```c++
class TreeAncestor {
  int n;
  int m;
  vector<int> depth;
  void dfs(int node, int parent,
           const unordered_map<int, vector<array<int, 2>>> &graph) {
    pa[node][0] = parent;

    auto it = graph.find(node);
    if (it == graph.end()) {
      return;
    }
    for (const auto &[child, weight] : it->second) {
      if (child == parent)
        continue;
      depth[child] = depth[node] + 1;
      distance[child] = distance[node] + weight;
      dfs(child, node, graph);
    }
  }

public:
  vector<vector<int>> pa;
  vector<uint64_t> distance;

  explicit TreeAncestor(const vector<vector<int>> &edges)
      : n(edges.size() + 1), m(32 - __builtin_clz(n)), depth(n, 0),
        pa(n, vector<int>(m, -1)), distance(n, 0) {
    unordered_map<int, vector<array<int, 2>>> graph(n);
    for (const auto &edge : edges) {
      int u = edge[0], v = edge[1], w = edge[2];
      graph[u].push_back({v, w});
      graph[v].push_back({u, w});
    }

    dfs(0, -1, graph);
    for (int j = 1; j < m; ++j) {
      for (int i = 0; i < n; ++i) {
        if (pa[i][j - 1] != -1) {
          pa[i][j] = pa[pa[i][j - 1]][j - 1];
        }
      }
    }
  }

  ~TreeAncestor() = default;

  int getKthAncestor(int node, int k) {
    for (; k > 0 && node != -1; k &= k - 1) {
      node = pa[node][31 - __builtin_clz(k & -k)];
    }
    return node;
  }

  int getLCA(int u, int v) {
    if (depth[u] > depth[v])
      swap(u, v);
    int diff = depth[v] - depth[u];
    v = getKthAncestor(v, diff);
    if (u == v)
      return u;
    for (int j = m - 1; j >= 0; --j) {
      if (pa[u][j] != pa[v][j]) {
        u = pa[u][j];
        v = pa[v][j];
      }
    }
    return pa[u][0];
  }

  int getDistance(int u, int v) {
    int lca = getLCA(u, v);
    return distance[u] + distance[v] - 2 * distance[lca];
  }

  int findDistance(int u, uint64_t d) {
    d = distance[u] - d;
    for (int j = m - 1; j >= 0; --j) {
      int p = pa[u][j];
      if (p != -1 && distance[p] >= d) {
        u = p;
      }
    }
    return u;
  }
};
```

```java
class TreeAncestor {
    public final int[][] pa;
    private final int[] depth;
    public final long[] distance;
    private final int m;

    private void dfs(int node, int parent, Map<Integer, Integer>[] graph) {
        pa[node][0] = parent;
        if (graph[node] == null) {
            return;
        }
        // graph foreach
        for (Map.Entry<Integer, Integer> entry : graph[node].entrySet()) {
            int c = entry.getKey(), w = entry.getValue();
            if (c == parent) continue;
            depth[c] = depth[node] + 1;
            distance[c] = distance[node] + w;
            dfs(c, node, graph);
        }
    }
    public TreeAncestor(int[][] edges) {
        int n = edges.length + 1;
        m = 32 - Integer.numberOfLeadingZeros(n);

        pa = new int[n][m];
        depth = new int[n];
        Arrays.fill(depth, 0);
        distance = new long[n];
        Arrays.fill(distance, 0);

        Map<Integer, Integer>[] graph = new Map[n];
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            graph[u] = graph[u] == null ? new HashMap<>() : graph[u];
            graph[u].put(v, w);
            graph[v] = graph[v] == null ? new HashMap<>() : graph[v];
            graph[v].put(u, w);
        }

        dfs(0, -1, graph);

        for (int j = 1; j < m; j++) {
            for (int i = 0; i < n; i++) {
                if (pa[i][j - 1] != -1) {
                    pa[i][j] = pa[pa[i][j - 1]][j - 1];
                } else {
                    pa[i][j] = -1;
                }
            }
        }
    }

    public int getKthAncestor(int node, int k) {
        for (; node != -1 && k > 0; k &= k - 1) {
            node = pa[node][Integer.numberOfTrailingZeros(k&-k)];
        }
        return node;
    }

    public int getLCA(int u, int v) {
        if (depth[u] > depth[v]) {
            int tmp = u;
            u = v;
            v = tmp;
        }
        v = getKthAncestor(v, depth[v] - depth[u]);
        if (v == u) {
            return u;
        }
        for (int j = m - 1; j >= 0; j--) {
            if (pa[u][j] != pa[v][j]) {
                u = pa[u][j];
                v = pa[v][j];
            }
        }
        return pa[u][0];
    }

    public int findDistance(int u, long d) {
        d = distance[u] - d;
        for (int j = m-1; j >= 0; --j) {
            int p = pa[u][j];
            if (p != -1 && distance[p] >= d) {
                u = p;
            }
        }
        return u;
    }
}
```

### 2. **区间最值查询（RMQ）**

- **问题**：多次查询数组某个区间的最小值/最大值。
- **倍增实现**：
    1. 构建稀疏表 `st[k][i]`，表示从 `i` 开始长度为 $`2^k`$ 的区间最值。
    2. 查询区间 `[L, R]` 时，取最大的 $`k`$ 使得 $`2^k \leq R-L+1`$，比较 `st[k][L]` 和 `st[k][R-2^k+1]`。
- **时间复杂度**：预处理 $`O(n \log n)`$，查询 $`O(1)`$。

### 快速幂

- **问题**：高效计算 $`a^b \mod p`$。
- **倍增实现**：
    1. 将指数 $`b`$ 分解为二进制形式。
    2. 通过累乘 $`a^{2^k}`$ 快速计算结果。
- **时间复杂度**：$`O(\log b)`$。

快速幂算法用于高效计算大整数幂或幂取模，时间复杂度为 $`O(\log n)`$。

#### **Python 模板**

```python
def fast_power(a: int, b: int, mod: int = None) -> int:
    """
    计算 a^b 或 (a^b) % mod
    :param a: 底数
    :param b: 指数（非负整数）
    :param mod: 可选模数
    :return: a^b 或 (a^b) % mod
    """
    result = 1
    a = a % mod if mod else a  # 初始取模（若提供mod）
    while b > 0:
        if b % 2 == 1:  # 当前二进制位为1
            result = result * a
            if mod: result %= mod
        a = a * a  # 基数平方
        if mod: a %= mod
        b //= 2  # 右移一位
    return result


# 示例
print(fast_power(2, 10))  # 输出 1024
print(fast_power(2, 10, 1000))  # 输出 24 (1024 % 1000)
```

```go
package main

import "fmt"

func fastPower(a, b, mod int) int {
    result := 1
    a = a % mod // 初始取模（若mod > 0）
    for b > 0 {
        if b%2 == 1 { // 当前二进制位为1
            result = (result * a) % mod
        }
        a = (a * a) % mod // 基数平方
        b /= 2           // 右移一位
    }
    return result
}

func main() {
    fmt.Println(fastPower(2, 10, 0))    // 输出 1024（mod=0时不取模）
    fmt.Println(fastPower(2, 10, 1000)) // 输出 24
}
```

#### 矩阵快速幂

矩阵快速幂是一种高效解决线性递推问题的算法，通过将递推关系转化为矩阵乘法形式，利用快速幂将时间复杂度从 $`O(n)`$ 优化到 $
`O(\log n)`$。以下是其核心原理和实现方法：

**通用步骤**

**1. 确定递推阶数**

对于 $`k`$ 阶线性递推（如 $`F(n) = a_1F(n-1) + \dots + a_kF(n-k)`$），构造 $`k \times k`$ 的转移矩阵。

**2. 构造转移矩阵**

- 第 $`i`$ 行表示如何从 $`F(n-i)`$ 推导到 $`F(n-i+1)`$。
- 例如，斐波那契数列的转移矩阵为：
  $$
  \begin{bmatrix}
  1 & 1 \\
  1 & 0
  \end{bmatrix}
  $$

**3. 初始状态向量**

根据递推的初始条件定义初始向量：
$$
\text{初始状态} =
\begin{bmatrix}
F(k-1) \\
F(k-2) \\
\vdots \\
F(0)
\end{bmatrix}
$$

**4. 计算矩阵幂**

通过快速幂计算 $`\text{转移矩阵}^{n}`$，再与初始状态相乘得到结果。

```go
func fib(n int) int {
    if n == 0 {
        return 0
    }
    // 转移矩阵
    mat := [][]int{{1, 1}, {1, 0}}
    // 计算 mat^(n-1)
    res := matrixPower(mat, n-1)
    // 初始状态 [F(1), F(0)] = [1, 0]
    return res[0][0] * 1 + res[0][1] * 0
}
```

**应用场景**

1. **线性递推问题**：如斐波那契数列、爬楼梯问题。
2. **动态规划优化**：将状态转移方程转化为矩阵形式。
3. **图论中的路径计数**：邻接矩阵的幂表示路径数。

**推广到 k 阶递推**

对于 $`k`$ 阶递推 $`F(n) = a_1F(n-1) + a_2F(n-2) + \dots + a_kF(n-k)`$，转移矩阵为：
$$
\begin{bmatrix}
a_1 & a_2 & \dots & a_{k-1} & a_k \\
1 & 0 & \dots & 0 & 0 \\
0 & 1 & \dots & 0 & 0 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \dots & 1 & 0
\end{bmatrix}
$$
初始状态向量为：
$$
\begin{bmatrix}
F(k-1) \\
F(k-2) \\
\vdots \\
F(0)
\end{bmatrix}
$$

1. **构造矩阵**：将递推关系转化为矩阵乘法形式。
2. **快速幂加速**：通过矩阵快速幂将线性递推的时间复杂度优化到对数级。
3. **通用性强**：适用于任何线性递推关系，只需调整转移矩阵和初始状态。

```python
from typing import List


# 矩阵快速幂
# a @ b，其中 @ 是矩阵乘法
def mul(a: List[List[int]], b: List[List[int]], mod: int) -> List[List[int]]:
    return [[sum(x * y for x, y in zip(row, col)) % mod for col in zip(*b)]
            for row in a]


# a^n @ f0
def pow_mul(a: List[List[int]], n: int, f0: List[List[int]], mod: int = 1000_000_007) -> List[List[int]]:
    res = f0
    while n:
        if n & 1:
            res = mul(a, res, mod)
        a = mul(a, a, mod)
        n >>= 1
    return res
```

## **优势与局限**

- **优势**：将线性时间的查询优化到对数时间。
- **局限**：需要额外的空间存储跳转表（如 $`O(n \log n)`$ 的稀疏表）。
- **适用场景**：适用于**静态数据**（预处理后数据不变）的多次查询问题。

理解倍增的核心在于掌握**二进制分解**和**跳转表的预处理逻辑**，它是高效解决许多算法问题的关键技巧。
