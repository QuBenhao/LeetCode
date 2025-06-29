package problem3600

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

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

func CopyUnionFind(uf *UnionFind) *UnionFind {
	newUf := &UnionFind{
		parent: make([]int, len(uf.parent)),
		rank:   make([]int, len(uf.rank)),
		cc:     uf.cc,
	}
	copy(newUf.parent, uf.parent)
	copy(newUf.rank, uf.rank)
	return newUf
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

func maxStability(n int, edges [][]int, k int) int {
	allUf := NewUnionFind(n)
	uf := NewUnionFind(n)
	var mustEdges, optionalEdges [][]int
	right := 200000
	for _, edge := range edges {
		u, v, w, must := edge[0], edge[1], edge[2], edge[3]
		if must == 1 {
			mustEdges = append(mustEdges, []int{u, v})
			if !uf.Union(u, v) {
				return -1
			}
			right = min(right, w)
		} else {
			optionalEdges = append(optionalEdges, []int{u, v, w})
		}
		allUf.Union(u, v)
	}
	if allUf.cc > 1 {
		return -1
	}

	sort.Slice(optionalEdges, func(i, j int) bool {
		return optionalEdges[i][2] > optionalEdges[j][2]
	})

	helper := func(mid int) bool {
		curUf := CopyUnionFind(uf)
		idx := 0
		for idx < len(optionalEdges) && optionalEdges[idx][2] >= mid {
			u, v := optionalEdges[idx][0], optionalEdges[idx][1]
			if curUf.Union(u, v) {
				if curUf.cc == 1 {
					return true
				}
			}
			idx++
		}
		remain := k
		mid = (mid + 1) / 2
		for idx < len(optionalEdges) && optionalEdges[idx][2] >= mid && remain > 0 {
			u, v := optionalEdges[idx][0], optionalEdges[idx][1]
			if curUf.Union(u, v) {
				if curUf.cc == 1 {
					return true
				}
				remain--
			}
			idx++
		}
		return curUf.cc == 1
	}

	left := 1
	for left < right {
		mid := left + (right-left+1)/2
		if helper(mid) {
			left = mid
		} else {
			right = mid - 1
		}
	}
	return left
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

	return maxStability(n, edges, k)
}
