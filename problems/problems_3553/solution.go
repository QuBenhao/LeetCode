package problem3553

import (
	"encoding/json"
	"log"
	"math/bits"
	"strings"
)

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

func minimumWeight(edges [][]int, queries [][]int) []int {
	ta := Constructor(edges)
	results := make([]int, len(queries))
	for i, query := range queries {
		u, v, d := query[0], query[1], query[2]
		results[i] = (ta.GetDistance(u, v) + ta.GetDistance(v, d) + ta.GetDistance(u, d)) / 2
	}
	return results
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

	return minimumWeight(edges, queries)
}
