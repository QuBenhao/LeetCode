package problem3342

import (
	"container/heap"
	"encoding/json"
	"log"
	"math"
	"strings"
)

func minTimeToReach(moveTime [][]int) int {
	m, n := len(moveTime), len(moveTime[0])
	directions := [][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	explored := make([][]int, m)
	for i := range explored {
		explored[i] = make([]int, n)
		for j := range explored[i] {
			explored[i][j] = math.MaxInt
		}
	}
	pq := &queue{}
	heap.Init(pq)
	heap.Push(pq, tuple{0, 0, 0})
	explored[0][0] = 0
	for pq.Len() > 0 {
		tp := heap.Pop(pq).(tuple)
		time, x, y := tp.time, tp.x, tp.y
		if x == m-1 && y == n-1 {
			return time
		}
		if time > explored[x][y] {
			continue
		}
		for _, d := range directions {
			nx, ny := x+d[0], y+d[1]
			if nx < 0 || nx >= m || ny < 0 || ny >= n {
				continue
			}
			nt := max(time, moveTime[nx][ny]) + (x+y)%2 + 1
			if nt < explored[nx][ny] {
				explored[nx][ny] = nt
				heap.Push(pq, tuple{nt, nx, ny})
			}
		}
	}
	return -1
}

type tuple struct{ time, x, y int }
type queue []tuple

func (q queue) Len() int { return len(q) }
func (q queue) Less(i, j int) bool {
	return q[i].time < q[j].time
}
func (q queue) Swap(i, j int) {
	q[i], q[j] = q[j], q[i]
}
func (q *queue) Push(x any) {
	*q = append(*q, x.(tuple))
}
func (q *queue) Pop() any {
	old := *q
	n := len(old)
	x := old[n-1]
	*q = old[0 : n-1]
	return x
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var moveTime [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &moveTime); err != nil {
		log.Fatal(err)
	}

	return minTimeToReach(moveTime)
}
