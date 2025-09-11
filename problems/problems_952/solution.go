package problem952

import (
	"encoding/json"
	"log"
	"strings"
)

const MAX_N = 100000

var PRIMES [][]int

func init() {
	PRIMES = make([][]int, MAX_N+1)
	for i := 2; i <= MAX_N; i++ {
		if len(PRIMES[i]) == 0 {
			for j := i; j <= MAX_N; j += i {
				PRIMES[j] = append(PRIMES[j], i)
			}
		}
	}
}

type UnionFind struct {
	parent []int
	rank   []int
	size   []int
	cc     int
}

func NewUnionFind(size int) *UnionFind {
	uf := &UnionFind{
		parent: make([]int, size),
		rank:   make([]int, size),
		size:   make([]int, size),
		cc:     size,
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

func largestComponentSize(nums []int) (ans int) {
	n := len(nums)
	uf := NewUnionFind(n)
	primeIdx := make(map[int]int)
	for i, num := range nums {
		for _, p := range PRIMES[num] {
			if j, ok := primeIdx[p]; ok {
				uf.Union(i, j)
			}
			primeIdx[p] = i
		}
	}
	for i := range n {
		ans = max(ans, uf.size[i])
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return largestComponentSize(nums)
}
