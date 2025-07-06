package problem3608

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func minTime(n int, edges [][]int, k int) int {
	sort.Slice(edges, func(i, j int) bool {
		return edges[i][2] > edges[j][2]
	})
	uf := NewUnionFind(n)
	for _, edge := range edges {
		uf.Union(edge[0], edge[1])
		if uf.cc < k {
			return edge[2]
		}
	}
	return 0
}

type UnionFind struct {
	parent []int
	rank   []int
	cc     int
}

func NewUnionFind(size int) *UnionFind {
	uf := &UnionFind{
		parent: make([]int, size),
		rank:   make([]int, size),
		cc:     size,
	}
	for i := range uf.parent {
		uf.parent[i] = i
		uf.rank[i] = 1
	}
	return uf
}

func (uf *UnionFind) Find(x int) int {
	for uf.parent[x] != x {
		uf.parent[x] = uf.parent[uf.parent[x]] // 路径压缩
		x = uf.parent[x]
	}
	return x
}

func (uf *UnionFind) Union(x, y int) bool {
	rootX := uf.Find(x)
	rootY := uf.Find(y)

	if rootX == rootY {
		return false // 已经在同一集合
	}

	// 按秩合并
	if uf.rank[rootX] > uf.rank[rootY] {
		uf.parent[rootY] = rootX
	} else {
		uf.parent[rootX] = rootY
		if uf.rank[rootX] == uf.rank[rootY] {
			uf.rank[rootY]++
		}
	}
	uf.cc-- // 合并后集合数减少
	return true
}

func (uf *UnionFind) IsConnected(x, y int) bool {
	return uf.Find(x) == uf.Find(y)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var edges [][]int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &edges); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return minTime(n, edges, k)
}
