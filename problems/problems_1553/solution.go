package problem1553

import (
	"container/heap"
	"encoding/json"
	"log"
	"strings"
)

func minDays(n int) int {
	dis := map[int]int{}
	h := &hp{{0, n}}
	for {
		p := heap.Pop(h).(pair)
		dx, x := p.d, p.x
		if x <= 1 {
			return dx + x
		}
		if dx > dis[x] {
			continue
		}
		for d := 2; d <= 3; d++ {
			y := x / d
			dy := dx + x%d + 1
			if dis[y] == 0 || dy < dis[y] {
				dis[y] = dy
				heap.Push(h, pair{dy, y})
			}
		}
	}
}

type pair struct{ d, x int }
type hp []pair

func (h hp) Len() int           { return len(h) }
func (h hp) Less(i, j int) bool { return h[i].d < h[j].d }
func (h hp) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(v any)        { *h = append(*h, v.(pair)) }
func (h *hp) Pop() any          { a := *h; v := a[len(a)-1]; *h = a[:len(a)-1]; return v }

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var n int

	if err := json.Unmarshal([]byte(values[0]), &n); err != nil {
		log.Fatal(err)
	}

	return minDays(n)
}
