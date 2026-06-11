package problem3559

import (
	"encoding/json"
	"log"
	"strings"
)

const MOD int64 = 1e9 + 7

// TreeAncestor 使用扁平化数组存储倍增信息
type TreeAncestor struct {
	depth  []int // depth[i] = i 到根的距离
	parent []int // parent[i] = i 的父节点
	jump   []int // 扁平化的倍增表：jump[node*m + k] = node 的 2^k 祖先
	m      int   // log n
}

// Constructor 构建 TreeAncestor
// 时间复杂度：O(n log n)，空间复杂度：O(n log n)
func Constructor(edges [][]int) TreeAncestor {
	n := len(edges) + 1

	// 建图：每个节点存储邻居列表
	degs := make([]int, n)
	for _, e := range edges {
		degs[e[0]-1]++
		degs[e[1]-1]++
	}

	graph := make([][]int, n)
	for i := range graph {
		graph[i] = make([]int, degs[i])
	}

	for _, e := range edges {
		u, v := e[0]-1, e[1]-1
		degs[u]--
		degs[v]--
		graph[u][degs[u]] = v
		graph[v][degs[v]] = u
	}

	// DFS 预处理深度和父节点（迭代版避免栈溢出）
	depth := make([]int, n)
	parent := make([]int, n)
	visited := make([]bool, n)

	type frame struct {
		node int
		iter int
	}
	stack := make([]frame, 0, n)
	stack = append(stack, frame{node: 0, iter: 0})

	for len(stack) > 0 {
		f := &stack[len(stack)-1]
		if f.iter == 0 {
			visited[f.node] = true
		}

		foundUnvisited := false
		for f.iter < len(graph[f.node]) {
			child := graph[f.node][f.iter]
			f.iter++
			if !visited[child] {
				depth[child] = depth[f.node] + 1
				parent[child] = f.node
				stack = append(stack, frame{node: child, iter: 0})
				foundUnvisited = true
				break
			}
		}

		if !foundUnvisited {
			stack = stack[:len(stack)-1]
		}
	}

	// 计算 m = ceil(log2(n))
	m := 0
	for (1 << m) < n {
		m++
	}

	// 扁平化倍增表
	jump := make([]int, n*m)
	for i := 0; i < n; i++ {
		jump[i*m+0] = parent[i]
	}

	for j := 1; j < m; j++ {
		for i := 0; i < n; i++ {
			prev := jump[i*m+(j-1)]
			if prev == -1 {
				jump[i*m+j] = -1
			} else {
				jump[i*m+j] = jump[prev*m+(j-1)]
			}
		}
	}

	return TreeAncestor{
		depth:  depth,
		parent: parent,
		jump:   jump,
		m:      m,
	}
}

// getLCA 使用倍增法求 LCA，O(log n)
func (ta *TreeAncestor) getLCA(u, v int) int {
	if u == v {
		return u
	}
	if ta.depth[u] < ta.depth[v] {
		u, v = v, u
	}

	// 将 u 提升到与 v 同一深度
	diff := ta.depth[u] - ta.depth[v]
	for bit := 0; diff > 0; bit++ {
		if diff&1 == 1 && bit < ta.m {
			next := ta.jump[u*ta.m+bit]
			if next != -1 {
				u = next
			}
		}
		diff >>= 1
	}

	if u == v {
		return u
	}

	// 一起向上跳
	for bit := ta.m - 1; bit >= 0; bit-- {
		pu := ta.jump[u*ta.m+bit]
		pv := ta.jump[v*ta.m+bit]
		if pu != -1 && pu != pv {
			u = pu
			v = pv
		}
	}

	return ta.jump[u*ta.m+0]
}

// getDist 返回两点间边数距离
func (ta *TreeAncestor) getDist(u, v int) int {
	lca := ta.getLCA(u, v)
	return ta.depth[u] + ta.depth[v] - 2*ta.depth[lca]
}

// fastPow 快速幂计算 base^exp % MOD
func fastPow(base, exp int64) int64 {
	result := int64(1)
	base %= MOD
	for exp > 0 {
		if exp&1 == 1 {
			result = result * base % MOD
		}
		base = base * base % MOD
		exp >>= 1
	}
	return result
}

// assignEdgeWeights 主函数
// 时间复杂度：O(n log n) 预处理 + O(q log n) 查询
// 空间复杂度：O(n log n)，但使用一维数组更节省内存
func assignEdgeWeights(edges [][]int, queries [][]int) []int {
	ta := Constructor(edges)
	ans := make([]int, 0, len(queries))

	for _, q := range queries {
		u, v := q[0]-1, q[1]-1
		if u == v {
			ans = append(ans, 0)
			continue
		}
		dist := ta.getDist(u, v)
		if dist <= 0 {
			ans = append(ans, 0)
		} else {
			ans = append(ans, int(fastPow(2, int64(dist-1))))
		}
	}

	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var edges [][]int
	var queries [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &edges); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &queries); err != nil {
		log.Fatal(err)
	}

	return assignEdgeWeights(edges, queries)
}
