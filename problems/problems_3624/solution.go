package problem3624

import (
	"encoding/json"
	"log"
	"math/bits"
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

func popcountDepth(nums []int64, queries [][]int64) (ans []int) {
	popcount := func(num uint64) (cur int) {
		for num > 1 {
			cur++
			num = uint64(bits.OnesCount64(num))
		}
		return cur
	}
	n := len(nums)
	trees := make([]*FenwickTree, 6)
	for i := range 6 {
		trees[i] = NewFenwickTree(n)
	}
	for i, num := range nums {
		depth := popcount(uint64(num))
		trees[depth].Update(i+1, 1)
	}
	for _, query := range queries {
		if query[0] == 1 {
			l, r, depth := int(query[1]), int(query[2]), int(query[3])
			ans = append(ans, trees[depth].RangeQuery(l+1, r+1))
		} else {
			idx, val := int(query[1]), query[2]
			oldDepth := popcount(uint64(nums[idx]))
			newDepth := popcount(uint64(val))
			nums[idx] = val
			if oldDepth != newDepth {
				trees[oldDepth].Update(idx+1, -1)
				trees[newDepth].Update(idx+1, 1)
			}
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int64
	var queries [][]int64

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &queries); err != nil {
		log.Fatal(err)
	}

	return popcountDepth(nums, queries)
}
