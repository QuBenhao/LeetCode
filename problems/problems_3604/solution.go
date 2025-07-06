package problem3604

import (
	"container/heap"
	"encoding/json"
	"log"
	"math"
	"strings"
)

func minTime(n int, edges [][]int) int {
	graph := make([][][]int, n)
	for _, edge := range edges {
		graph[edge[0]] = append(graph[edge[0]], []int{edge[1], edge[2], edge[3]})
	}
	h := &hp{[]int{0, 0}} // {time, node}
	heap.Init(h)
	dist := make([]int, n)
	for i := range dist {
		dist[i] = math.MaxInt32
	}
	dist[0] = 0
	for h.Len() > 0 {
		cur := heap.Pop(h).([]int)
		time, node := cur[0], cur[1]
		if node == n-1 {
			return time
		}
		if time > dist[node] {
			continue
		}
		for _, next := range graph[node] {
			nextNode, start, end := next[0], next[1], next[2]
			if time <= end {
				nextTime := max(time, start) + 1
				if nextTime < dist[nextNode] {
					dist[nextNode] = nextTime
					heap.Push(h, []int{nextTime, nextNode})
				}
			}
		}
	}
	return -1
}

type hp [][]int

func (h hp) Len() int           { return len(h) }
func (h hp) Less(i, j int) bool { return h[i][0] < h[j][0] }
func (h hp) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(x any) {
	*h = append(*h, x.([]int))
}
func (h *hp) Pop() any {
	if len(*h) == 0 {
		return nil
	}
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var edges [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &edges); err != nil {
		log.Fatal(err)
	}

	return minTime(n, edges)
}
