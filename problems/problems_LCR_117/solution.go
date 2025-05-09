package problemLCR_117

import (
	"encoding/json"
	"log"
	"strings"
)

type UnionFind struct {
	parent []int
	rank   []int
}

func NewUnionFind(size int) *UnionFind {
	uf := &UnionFind{
		parent: make([]int, size),
		rank:   make([]int, size),
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
	return true
}

func (uf *UnionFind) IsConnected(x, y int) bool {
	return uf.Find(x) == uf.Find(y)
}

func numSimilarGroups(strings []string) (ans int) {
	n := len(strings)
	uf := NewUnionFind(n)
	isSimilar := func(a, b string) bool {
		diff := 0
		for i := 0; i < len(a); i++ {
			if a[i] != b[i] {
				diff++
				if diff > 2 {
					return false
				}
			}
		}
		return diff == 2 || diff == 0
	}
	for i, s := range strings {
		for j := i + 1; j < n; j++ {
			if isSimilar(s, strings[j]) {
				uf.Union(i, j)
			}
		}
	}
	for i := range n {
		if uf.parent[i] == i {
			ans++
		}
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var strs []string

	if err := json.Unmarshal([]byte(inputValues[0]), &strs); err != nil {
		log.Fatal(err)
	}

	return numSimilarGroups(strs)
}
