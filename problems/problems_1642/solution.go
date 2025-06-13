package problem1642

import (
	"container/heap"
	"encoding/json"
	"log"
	"strings"
)

func furthestBuilding(heights []int, bricks int, ladders int) int {
	maxHeap := &MaxHeap{}
	heap.Init(maxHeap)
	n := len(heights)
	for i := range n - 1 {
		if heights[i] >= heights[i+1] {
			continue
		}
		if diff := heights[i+1] - heights[i]; bricks >= diff {
			bricks -= diff
			heap.Push(maxHeap, diff)
		} else {
			if ladders > 0 {
				if maxHeap.Len() > 0 && diff < (*maxHeap)[0] {
					// Use a ladder for the current building and replace the largest brick usage
					bricks += (*maxHeap)[0] - diff
					heap.Pop(maxHeap)
					heap.Push(maxHeap, diff)
				}
				// Use a ladder
				ladders--
			} else {
				// No bricks or ladders left, return the current index
				return i
			}
		}
	}
	return n - 1
}

type MaxHeap []int

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *MaxHeap) Push(x any) {
	*h = append(*h, x.(int))
}
func (h *MaxHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var heights []int
	var bricks int
	var ladders int

	if err := json.Unmarshal([]byte(inputValues[0]), &heights); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &bricks); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &ladders); err != nil {
		log.Fatal(err)
	}

	return furthestBuilding(heights, bricks, ladders)
}
