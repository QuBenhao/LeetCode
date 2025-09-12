package problem827

import (
	"encoding/json"
	"log"
	"strings"
)

type UnionFind struct {
	parent []int
	rank   []int
	size   []int
	cc     int
}

func NewUnionFind(n int) *UnionFind {
	uf := &UnionFind{
		parent: make([]int, n),
		rank:   make([]int, n),
		size:   make([]int, n),
		cc:     n,
	}
	for i := range uf.parent {
		uf.parent[i] = i
		uf.rank[i] = 1
		uf.size[i] = 1
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
		uf.size[rootX] += uf.size[rootY]
	} else {
		uf.parent[rootX] = rootY
		if uf.rank[rootX] == uf.rank[rootY] {
			uf.rank[rootY]++
		}
		uf.size[rootY] += uf.size[rootX]
	}
	uf.cc-- // 合并后集合数减少
	return true
}

func (uf *UnionFind) IsConnected(x, y int) bool {
	return uf.Find(x) == uf.Find(y)
}

func (uf *UnionFind) GetSize(x int) int {
	return uf.size[uf.Find(x)]
}

var DIRS = [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}

func largestIsland(grid [][]int) (ans int) {
	n := len(grid)
	pointToIdx := func(x int, y int) int {
		return x*n + y
	}

	uf := NewUnionFind(n * n)
	for i := range n {
		for j := range n {
			if grid[i][j] == 0 {
				continue
			}
			p := pointToIdx(i, j)
			for _, dir := range DIRS {
				nx, ny := i+dir[0], j+dir[1]
				if nx < 0 || nx == n || ny < 0 || ny == n || grid[nx][ny] == 0 {
					continue
				}
				uf.Union(p, uf.Find(pointToIdx(nx, ny)))
			}
			ans = max(ans, uf.GetSize(p))
		}
	}
	for i := range n {
		for j := range n {
			if grid[i][j] != 0 {
				continue
			}
			tot := 1
			explored := map[int]bool{}
			for _, dir := range DIRS {
				nx, ny := i+dir[0], j+dir[1]
				if nx < 0 || nx == n || ny < 0 || ny == n || grid[nx][ny] == 0 {
					continue
				}
				root := uf.Find(pointToIdx(nx, ny))
				if _, ok := explored[root]; ok {
					continue
				}
				explored[root] = true
				tot += uf.GetSize(root)
			}
			ans = max(ans, tot)
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return largestIsland(grid)
}
