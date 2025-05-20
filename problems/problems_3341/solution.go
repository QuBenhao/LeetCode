package problem3341

import (
	"container/heap"
	"encoding/json"
	"log"
	"strings"
)

func minTimeToReach(moveTime [][]int) int {
	m, n := len(moveTime), len(moveTime[0])
	directions := [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	visited := make([][]bool, m)
	for i := range visited {
		visited[i] = make([]bool, n)
	}
	pq := &hp{}
	heap.Init(pq)
	heap.Push(pq, tuple{0, 0, 0})
	for pq.Len() > 0 {
		cur := heap.Pop(pq).(tuple)
		time, x, y := cur.dis, cur.x, cur.y
		if x == m-1 && y == n-1 {
			return time
		}
		if visited[x][y] {
			continue
		}
		visited[x][y] = true
		for _, d := range directions {
			newX, newY := x+d[0], y+d[1]
			if newX >= 0 && newX < m && newY >= 0 && newY < n {
				newTime := max(time, moveTime[newX][newY]) + 1
				if !visited[newX][newY] {
					heap.Push(pq, tuple{newTime, newX, newY})
				}
			}
		}
	}
	return -1
}

type tuple struct{ dis, x, y int }
type hp []tuple

func (h hp) Len() int           { return len(h) }
func (h hp) Less(i, j int) bool { return h[i].dis < h[j].dis }
func (h hp) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(v any)        { *h = append(*h, v.(tuple)) }
func (h *hp) Pop() (v any)      { a := *h; *h, v = a[:len(a)-1], a[len(a)-1]; return }

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var moveTime [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &moveTime); err != nil {
		log.Fatal(err)
	}

	return minTimeToReach(moveTime)
}
