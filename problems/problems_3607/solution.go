package problem3607

import (
	"container/list"
	"encoding/json"
	"log"
	"strings"
)

func processQueries(c int, connections [][]int, queries [][]int) (ans []int) {
	uf := NewUnionFind(c)
	for _, conn := range connections {
		uf.Union(conn[0]-1, conn[1]-1)
	}
	mapping := make(map[int]*list.List)
	elemMap := make(map[int]*list.Element)
	for i := range c {
		root := uf.Find(i)
		if _, exists := mapping[root]; !exists {
			mapping[root] = list.New()
		}
		mapping[root].PushBack(i + 1) // 使用1-based索引
		elemMap[i] = mapping[root].Back()
	}
	for _, query := range queries {
		op, x := query[0], query[1]-1
		root := uf.Find(x)
		if op == 2 {
			node := elemMap[x]
			if node != nil {
				elemMap[x] = nil
				mapping[root].Remove(node)
			}
		} else {
			if mapping[root].Len() == 0 {
				ans = append(ans, -1)
			} else {
				node := elemMap[x]
				if node == nil {
					node = mapping[root].Front()
				}
				ans = append(ans, node.Value.(int))
			}
		}
	}
	return
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
	var c int
	var connections [][]int
	var queries [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &c); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &connections); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &queries); err != nil {
		log.Fatal(err)
	}

	return processQueries(c, connections, queries)
}
