# Doubling

Doubling is an algorithmic technique that **preprocesses data and uses binary decomposition to speed up queries**. Its central idea is to build a **jump table** (such as a sparse
table), reducing each query or operation from linear to logarithmic time, such as $`O(\log n)`$. The main principles and applications are described below:

## **Core principles of doubling**

1. **Binary decomposition**  
   Break the problem into **exponentially increasing step sizes** (such as $`2^0, 2^1, 2^2, \dots`$). For example, a jump table stores the result of taking $`2^k`$
   steps from each position.

2. **Preprocess the jump table**  
   Build a two-dimensional array `dp[k][i]` containing the destination or result after taking $`2^k`$ steps from position `i`. For example:
    - `dp[0][i]` stores the result after 1 step ($`2^0 = 1`$).
    - `dp[k][i] = dp[k-1][ dp[k-1][i] ]` builds the jump table recursively.

3. **Fast queries**  
   Express the requested number of steps in binary and combine jumps for its set bits. For example, 13 steps (binary `1101`) can be decomposed into $`8 + 4 + 1`$ steps, taking jumps of $
   `2^3, 2^2, 2^0`$ steps in sequence.

## **Typical applications**

### Fast exponentiation
```c++
int fast_pow(int64_t base, int64_t exp, int64_t mod) {
  int64_t res = 1;
  while (exp) {
    if (exp & 1) res = (1LL * res * base) % mod;
    base = (1LL * base * base) % mod;
    exp >>= 1;
  }
  return static_cast<int>(res);
}
```

### Lowest common ancestor

- **Problem**: Quickly find the lowest common ancestor of two nodes in a tree.
- **Implementation using doubling**:
    1. Precompute the $`2^k`$-th ancestor of each node (`up[k][u]`).
    2. Bring both nodes to the same depth, then move them upward together until their common ancestor is found.
- **Time complexity**: $`O(n \log n)`$ preprocessing and $`O(\log n)`$ per query.
- **Example**: [3553.包含给定路径的最小带权子树 II](problems/problems_3553/problem_zh.md)

```c++
class LcaBinaryLifting {
    vector<int> depth;
    vector<long long> dis; // For an unweighted tree (edge weights of 1), use depth instead of dis
    vector<vector<int>> pa;

public:
    LcaBinaryLifting(vector<vector<int>>& edges) {
        int n = edges.size() + 1;
        int m = bit_width((unsigned) n); // Number of bits in n
        vector<vector<pair<int, int>>> g(n);
        for (auto& e : edges) {
            // If node labels start at 1, use x=e[0]-1 and y=e[1]-1
            int x = e[0], y = e[1], w = e[2];
            g[x].emplace_back(y, w);
            g[y].emplace_back(x, w);
        }

        depth.resize(n);
        dis.resize(n);
        pa.resize(m, vector<int>(n, -1));

        auto dfs = [&](this auto&& dfs, int x, int fa) -> void {
            pa[0][x] = fa;
            for (auto& [y, w] : g[x]) {
                if (y != fa) {
                    depth[y] = depth[x] + 1;
                    dis[y] = dis[x] + w;
                    dfs(y, x);
                }
            }
        };
        dfs(0, -1);

        for (int i = 0; i < m - 1; i++) {
            for (int x = 0; x < n; x++) {
                if (int p = pa[i][x]; p != -1) {
                    pa[i + 1][x] = pa[i][p];
                }
            }
        }
    }

    // Return the k-th ancestor of node
    // Return -1 if it does not exist
    int get_kth_ancestor(int node, int k) {
        for (; k > 0 && node >= 0; k &= k - 1) {
            node = pa[countr_zero((unsigned) k)][node];
        }
        return node;
    }

    // Return the lowest common ancestor of x and y (node labels start at 0)
    int get_lca(int x, int y) {
        if (depth[x] > depth[y]) {
            swap(x, y);
        }
        y = get_kth_ancestor(y, depth[y] - depth[x]); // Bring y to the same depth as x
        if (y == x) {
            return x;
        }
        for (int i = pa.size() - 1; i >= 0; i--) {
            int px = pa[i][x], py = pa[i][y];
            if (px != py) {
                x = px;
                y = py; // Move both nodes up by 2^i steps
            }
        }
        return pa[0][x];
    }

    // Return the distance from x to y (shortest path length)
    long long get_dis(int x, int y) {
        return dis[x] + dis[y] - dis[get_lca(x, y)] * 2;
    }
};
```
```python
from typing import List


class TreeAncestor:
    def __init__(self, edges: List[List[int]]):
        n = len(edges) + 1
        m = n.bit_length()
        g = [[] for _ in range(n)]
        for x, y in edges:  # Node labels start at 0
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
            if k >> i & 1:  # Bit i of k, counted from the least significant bit, is 1
                node = self.pa[node][i]
        return node

    # Return the lowest common ancestor of x and y (node labels start at 0)
    def get_lca(self, x: int, y: int) -> int:
        if self.depth[x] > self.depth[y]:
            x, y = y, x
        # Bring y to the same depth as x
        y = self.get_kth_ancestor(y, self.depth[y] - self.depth[x])
        if y == x:
            return x
        for i in range(len(self.pa[x]) - 1, -1, -1):
            px, py = self.pa[x][i], self.pa[y][i]
            if px != py:
                x, y = px, py  # Move both nodes up by 2**i steps
        return self.pa[x][0]

    def get_dis(self, x: int, y: int) -> int:
        return self.depth[x] + self.depth[y] - self.depth[self.get_lca(x, y)] * 2
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

### 2. **Range minimum/maximum query (RMQ)**

- **Problem**: Repeatedly query the minimum or maximum value in an array interval.
- **Implementation using doubling**:
    1. Build a sparse table `st[k][i]` containing the minimum or maximum over the interval of length $`2^k`$ starting at `i`.
    2. To query `[L, R]`, choose the largest $`k`$ such that $`2^k \leq R-L+1`$ and compare `st[k][L]` with `st[k][R-2^k+1]`.
- **Time complexity**: $`O(n \log n)`$ preprocessing and $`O(1)`$ per query.

### Fast exponentiation

- **Problem**: Compute $`a^b \mod p`$ efficiently.
- **Implementation using doubling**:
    1. Express the exponent $`b`$ in binary.
    2. Multiply the corresponding powers $`a^{2^k}`$ to compute the result efficiently.
- **Time complexity**: $`O(\log b)`$.

Fast exponentiation computes large integer powers or modular powers in $`O(\log n)`$ time.

#### **Python template**

```python
def fast_power(a: int, b: int, mod: int = None) -> int:
    """
    Compute a^b or (a^b) % mod
    :param a: Base
    :param b: Exponent (a nonnegative integer)
    :param mod: Optional modulus
    :return: a^b or (a^b) % mod
    """
    result = 1
    a = a % mod if mod else a  # Reduce the base modulo mod if provided
    while b > 0:
        if b % 2 == 1:  # The current binary digit is 1
            result = result * a
            if mod: result %= mod
        a = a * a  # Square the base
        if mod: a %= mod
        b //= 2  # Shift right by one bit
    return result


# Example
print(fast_power(2, 10))  # Outputs 1024
print(fast_power(2, 10, 1000))  # Outputs 24 (1024 % 1000)
```

```go
package main

import "fmt"

func fastPower(a, b, mod int) int {
    result := 1
    a = a % mod // Reduce the base modulo mod (if mod > 0)
    for b > 0 {
        if b%2 == 1 { // The current binary digit is 1
            result = (result * a) % mod
        }
        a = (a * a) % mod // Square the base
        b /= 2           // Shift right by one bit
    }
    return result
}

func main() {
    fmt.Println(fastPower(2, 10, 0))    // Outputs 1024 (no modular reduction when mod=0)
    fmt.Println(fastPower(2, 10, 1000)) // Outputs 24
}
```

#### Fast matrix exponentiation

Fast matrix exponentiation solves linear recurrences efficiently. It expresses the recurrence as matrix multiplication and uses fast exponentiation to reduce the time complexity from $`O(n)`$ to $
`O(\log n)`$. Its main principles and implementation are described below:

**General steps**

**1. Determine the order of the recurrence**

For a linear recurrence of order $`k`$, such as $`F(n) = a_1F(n-1) + \dots + a_kF(n-k)`$, construct a $`k \times k`$ transition matrix.

**2. Construct the transition matrix**

- Row $`i`$ describes how to derive $`F(n-i+1)`$ from $`F(n-i)`$.
- For example, the transition matrix for the Fibonacci sequence is:
  $$
  \begin{bmatrix}
  1 & 1 \\
  1 & 0
  \end{bmatrix}
  $$

**3. Define the initial state vector**

Define the initial vector from the recurrence's initial conditions:
$$
\text{Initial state} =
\begin{bmatrix}
F(k-1) \\
F(k-2) \\
\vdots \\
F(0)
\end{bmatrix}
$$

**4. Compute the matrix power**

Use fast exponentiation to compute $`\text{transition matrix}^{n}`$, then multiply it by the initial state to obtain the result.

```go
func fib(n int) int {
    if n == 0 {
        return 0
    }
    // Transition matrix
    mat := [][]int{{1, 1}, {1, 0}}
    // Compute mat^(n-1)
    res := matrixPower(mat, n-1)
    // Initial state [F(1), F(0)] = [1, 0]
    return res[0][0] * 1 + res[0][1] * 0
}
```

**Applications**

1. **Linear recurrences**: Examples include the Fibonacci sequence and the climbing stairs problem.
2. **Dynamic programming optimization**: Express state transitions as a matrix.
3. **Counting paths in graphs**: Powers of the adjacency matrix give path counts.

**Generalization to recurrences of order k**

For a recurrence of order $`k`$, $`F(n) = a_1F(n-1) + a_2F(n-2) + \dots + a_kF(n-k)`$, the transition matrix is:
$$
\begin{bmatrix}
a_1 & a_2 & \dots & a_{k-1} & a_k \\
1 & 0 & \dots & 0 & 0 \\
0 & 1 & \dots & 0 & 0 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \dots & 1 & 0
\end{bmatrix}
$$
The initial state vector is:
$$
\begin{bmatrix}
F(k-1) \\
F(k-2) \\
\vdots \\
F(0)
\end{bmatrix}
$$

1. **Construct the matrix**: Express the recurrence as matrix multiplication.
2. **Accelerate with fast exponentiation**: Fast matrix exponentiation reduces a linear recurrence's computation time from linear to logarithmic.
3. **General applicability**: Any linear recurrence can use this method by adjusting the transition matrix and initial state.

```python
from typing import List


# Fast matrix exponentiation
# a @ b, where @ denotes matrix multiplication
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

## **Advantages and limitations**

- **Advantage**: Reduces query time from linear to logarithmic.
- **Limitation**: Requires extra space for the jump table, such as $`O(n \log n)`$ for a sparse table.
- **Use cases**: Repeated queries over **static data** that does not change after preprocessing.

Understanding doubling requires mastering **binary decomposition** and **jump table preprocessing**, which are useful techniques for solving many algorithm problems efficiently.
