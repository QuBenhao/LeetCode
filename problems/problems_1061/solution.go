package problem1061

import (
	"encoding/json"
	"log"
	"strings"
)

type UnionFind struct {
	parent []int
	size   []int
	cc     int
}

func NewUnionFind(n int) *UnionFind {
	parent := make([]int, n)
	size := make([]int, n)
	for i := range n {
		parent[i] = i
	}
	for i := range size {
		size[i] = 1
	}
	return &UnionFind{
		parent: parent,
		size:   size,
		cc:     n,
	}
}

func (uf *UnionFind) Find(x int) int {
	if uf.parent[x] != x {
		uf.parent[x] = uf.Find(uf.parent[x]) // Path compression
	}
	return uf.parent[x]
}

func (uf *UnionFind) Union(x int, y int) bool {
	px, py := uf.Find(x), uf.Find(y)
	if px == py {
		return false
	}

	father, child := min(px, py), max(px, py)
	uf.parent[child] = father
	uf.size[father] += uf.size[child]
	uf.cc--
	return true
}

func smallestEquivalentString(s1 string, s2 string, baseStr string) string {
	uf := NewUnionFind(26)
	for i := range s1 {
		uf.Union(int(s1[i]-'a'), int(s2[i]-'a'))
	}
	result := make([]byte, len(baseStr))
	for i := range baseStr {
		root := uf.Find(int(baseStr[i] - 'a'))
		result[i] = byte(root + 'a')
	}
	return string(result)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s1 string
	var s2 string
	var baseStr string

	if err := json.Unmarshal([]byte(inputValues[0]), &s1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &s2); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &baseStr); err != nil {
		log.Fatal(err)
	}

	return smallestEquivalentString(s1, s2, baseStr)
}
