package problem2179

import (
	"encoding/json"
	"log"
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

func goodTriplets(nums1 []int, nums2 []int) (ans int64) {
	n := len(nums1)
	idxMap := map[int]int{}
	for i, num := range nums1 {
		idxMap[num] = i
	}
	fenwickTree := NewFenwickTree(n)
	for i, num := range nums2 {
		idx := idxMap[num]
		less := fenwickTree.Query(idx)
		ans += int64(less) * int64(n-1-idx-(i-less))
		fenwickTree.Update(idx+1, 1)
	}
	return ans
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums1 []int
	var nums2 []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &nums2); err != nil {
		log.Fatal(err)
	}

	return goodTriplets(nums1, nums2)
}
