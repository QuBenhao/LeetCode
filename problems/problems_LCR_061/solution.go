package problemLCR_061

import (
	"container/heap"
	"encoding/json"
	"log"
	"strings"
)

func kSmallestPairs(nums1 []int, nums2 []int, k int) (ans [][]int) {
	n1, n2 := len(nums1), len(nums2)
	h := &IHeap{}
	heap.Init(h)
	for i := 0; i < n1; i++ {
		heap.Push(h, [3]int{nums1[i] + nums2[0], i, 0})
	}
	for idx := 0; h.Len() > 0 && idx < k; idx++ {
		top := heap.Pop(h).([3]int)
		ans = append(ans, []int{nums1[top[1]], nums2[top[2]]})
		if top[2]+1 < n2 {
			heap.Push(h, [3]int{nums1[top[1]] + nums2[top[2]+1], top[1], top[2] + 1})
		}
	}
	return
}

type IHeap [][3]int

func (h *IHeap) Len() int { return len(*h) }
func (h *IHeap) Less(i, j int) bool {
	return (*h)[i][0] < (*h)[j][0] || ((*h)[i][0] == (*h)[j][0] && (*h)[i][1] > (*h)[j][1])
}
func (h *IHeap) Swap(i, j int) { (*h)[i], (*h)[j] = (*h)[j], (*h)[i] }
func (h *IHeap) Push(x interface{}) {
	*h = append(*h, x.([3]int))
}
func (h *IHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums1 []int
	var nums2 []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &nums2); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return kSmallestPairs(nums1, nums2, k)
}
