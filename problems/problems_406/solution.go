package problem406

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

type FenwickTree struct {
	n    int
	tree []int
}

func NewFenwickTree(size int) *FenwickTree {
	return &FenwickTree{
		n:    size,
		tree: make([]int, size+1), // 索引从1开始
	}
}

func (ft *FenwickTree) lowbit(x int) int {
	return x & (-x)
}

func (ft *FenwickTree) Update(idx int, delta int) {
	for idx <= ft.n {
		ft.tree[idx] += delta
		idx += ft.lowbit(idx)
	}
}

func (ft *FenwickTree) Query(idx int) int {
	res := 0
	for idx > 0 {
		res += ft.tree[idx]
		idx -= ft.lowbit(idx)
	}
	return res
}

func (ft *FenwickTree) RangeQuery(l, r int) int {
	return ft.Query(r) - ft.Query(l-1)
}

func reconstructQueue(people [][]int) [][]int {
	slices.SortFunc(people, func(a, b []int) int {
		if a[0] == b[0] {
			return b[1] - a[1]
		}
		return a[0] - b[0]
	})
	n := len(people)
	fenwick := NewFenwickTree(n)
	ans := make([][]int, n)
	for _, person := range people {
		l, r := 1, n
		for l < r {
			mid := (l + r) / 2
			if fenwick.Query(mid) >= mid-person[1] {
				l = mid + 1
			} else {
				r = mid
			}
		}
		fenwick.Update(l, 1)
		ans[l-1] = person
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var people [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &people); err != nil {
		log.Fatal(err)
	}

	return reconstructQueue(people)
}
