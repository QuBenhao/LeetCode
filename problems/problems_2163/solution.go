package problem2163

import (
	"container/heap"
	"encoding/json"
	"log"
	"strings"
)

func minimumDifference(nums []int) int64 {
	n := len(nums) / 3
	pq := &minHeap{}
	suffixSum := int64(0)
	for i := 2 * n; i < len(nums); i++ {
		suffixSum += int64(nums[i])
		heap.Push(pq, nums[i])
	}
	suffixMax := make([]int64, n+1)
	suffixMax[n] = suffixSum
	for i := 2*n - 1; i >= n; i-- {
		heap.Push(pq, nums[i])
		suffixSum += int64(nums[i] - heap.Pop(pq).(int))
		suffixMax[i-n] = suffixSum
	}
	pq = &minHeap{}
	prefixSum := int64(0)
	for i := range n {
		prefixSum += int64(nums[i])
		heap.Push(pq, -nums[i])
	}
	ans := prefixSum - suffixMax[0]
	for i := n; i < 2*n; i++ {
		heap.Push(pq, -nums[i])
		prefixSum += int64(nums[i] + heap.Pop(pq).(int))
		ans = min(ans, prefixSum-suffixMax[i+1-n])
	}
	return ans
}

type minHeap []int

func (h minHeap) Len() int           { return len(h) }
func (h minHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h minHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(v any)        { *h = append(*h, v.(int)) }
func (h *minHeap) Pop() (v any)      { a := *h; *h, v = a[:len(a)-1], a[len(a)-1]; return }

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return minimumDifference(nums)
}
