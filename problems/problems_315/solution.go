package problem315

import (
	"cmp"
	"encoding/json"
	"log"
	"maps"
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

func countSmaller(nums []int) []int {
	n := len(nums)
	numsIdx := map[int]int{}
	for _, num := range nums {
		numsIdx[num] = 0
	}
	m := len(numsIdx)
	sorted := slices.SortedFunc(maps.Keys(numsIdx), func(a, b int) int { return cmp.Compare(a, b) })
	for i, num := range sorted {
		numsIdx[num] = i
	}
	ans := make([]int, n)
	fenwickTree := NewFenwickTree(m)
	for i := n - 1; i >= 0; i-- {
		idx := numsIdx[nums[i]]
		ans[i] = fenwickTree.Query(idx)
		fenwickTree.Update(idx+1, 1)
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return countSmaller(nums)
}
