package problemLCR_119

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

func longestConsecutive(nums []int) (ans int) {
	n := len(nums)
	s := make(map[int]int)
	for i, num := range nums {
		if _, ok := s[num]; ok {
			continue
		}
		s[num] = i
	}
	uf := NewUnionFind(n)
	for k, idx := range s {
		if i, ok := s[k-1]; ok {
			uf.Union(idx, i)
		}
		if i, ok := s[k+1]; ok {
			uf.Union(idx, i)
		}
	}
	sizeCounts := make(map[int]int)
	for i := range n {
		root := uf.Find(i)
		sizeCounts[root]++
		ans = max(ans, sizeCounts[root])
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return longestConsecutive(nums)
}
