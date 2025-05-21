package problem3362

import (
	"container/heap"
	"encoding/json"
	"log"
	"slices"
	"sort"
	"strings"
)

func maxRemoval(nums []int, queries [][]int) int {
	slices.SortFunc(queries, func(a, b []int) int { return a[0] - b[0] })
	h := &hp{}
	cur, j := 0, 0
	diff := make([]int, len(nums)+1)
	for i, num := range nums {
		cur += diff[i]
		for ; j < len(queries) && queries[j][0] <= i; j++ {
			heap.Push(h, queries[j][1])
		}
		for cur < num && h.Len() > 0 && h.IntSlice[0] >= i {
			cur++
			diff[heap.Pop(h).(int)+1]--
		}
		if cur < num {
			return -1
		}
	}
	return h.Len()
}

type hp struct{ sort.IntSlice }

func (h hp) Less(i, j int) bool { return h.IntSlice[i] > h.IntSlice[j] }
func (h *hp) Push(x any) {
	h.IntSlice = append(h.IntSlice, x.(int))
}
func (h *hp) Pop() any {
	n := h.IntSlice
	x := n[len(n)-1]
	h.IntSlice = n[:len(n)-1]
	return x
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var queries [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &queries); err != nil {
		log.Fatal(err)
	}

	return maxRemoval(nums, queries)
}
