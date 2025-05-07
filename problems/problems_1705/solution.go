package problem1705

import (
	"container/heap"
	"encoding/json"
	"log"
	"strings"
)

func eatenApples(apples []int, days []int) (ans int) {
	pq := &maxHeap{}
	heap.Init(pq)
	n := len(apples)
	for i := 0; i < n; i++ {
		heap.Push(pq, tuple{apples[i], days[i] + i})
		for pq.Len() > 0 && (*pq)[0].day <= i {
			heap.Pop(pq)
		}
		if pq.Len() > 0 {
			ans++
			(*pq)[0].apple--
			if (*pq)[0].apple == 0 {
				heap.Pop(pq)
			}
		}
	}
	cur := n
	for pq.Len() > 0 {
		for pq.Len() > 0 && (*pq)[0].day <= cur {
			heap.Pop(pq)
		}
		if pq.Len() == 0 {
			break
		}
		item := heap.Pop(pq).(tuple)
		diff := min(item.day-cur, item.apple)
		ans += diff
		cur += diff
	}
	return
}

type tuple struct{ apple, day int }
type maxHeap []tuple

func (h maxHeap) Len() int           { return len(h) }
func (h maxHeap) Less(i, j int) bool { return h[i].day < h[j].day }
func (h maxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *maxHeap) Push(x interface{}) {
	*h = append(*h, x.(tuple))
}
func (h *maxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var apples []int
	var days []int

	if err := json.Unmarshal([]byte(inputValues[0]), &apples); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &days); err != nil {
		log.Fatal(err)
	}

	return eatenApples(apples, days)
}
