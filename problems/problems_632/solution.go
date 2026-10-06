package problem632

import (
	"container/heap"
	"encoding/json"
	"log"
	"math"
	"strings"
)

func smallestRange(nums [][]int) []int {
	h := make(hp, len(nums))
	r := math.MinInt
	for i, arr := range nums {
		h[i] = tuple{arr[0], i, 0} // Push the first element of each list onto the heap
		r = max(r, arr[0])
	}
	heap.Init(&h)

	ansL, ansR := h[0].x, r            // Endpoints of the first valid range
	for h[0].j+1 < len(nums[h[0].i]) { // The list at the heap root has another element
		x := nums[h[0].i][h[0].j+1] // The next element of the list at the heap root
		r = max(r, x)               // Update the right endpoint of the valid range
		h[0].x = x                  // Replace the heap root
		h[0].j++
		heap.Fix(&h, 0)
		l := h[0].x // Left endpoint of the current valid range
		if r-l < ansR-ansL {
			ansL, ansR = l, r
		}
	}
	return []int{ansL, ansR}
}

type tuple struct{ x, i, j int }
type hp []tuple

func (h hp) Len() int           { return len(h) }
func (h hp) Less(i, j int) bool { return h[i].x < h[j].x }
func (h hp) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (hp) Push(any)             {} // Unused; this can be omitted
func (hp) Pop() (_ any)         { return }

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return smallestRange(nums)
}
