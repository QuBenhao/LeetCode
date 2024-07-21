package problem2101

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumDetonation(bombs [][]int) (ans int) {
	n := len(bombs)
	graph := make([][]int, n)
	for i := 0; i < n-1; i++ {
		x1, y1, r1 := bombs[i][0], bombs[i][1], bombs[i][2]
		r1 *= r1
		for j := i + 1; j < n; j++ {
			x2, y2, r2 := bombs[j][0], bombs[j][1], bombs[j][2]
			r2 *= r2
			dis := (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)
			if dis <= r1 {
				graph[i] = append(graph[i], j)
			}
			if dis <= r2 {
				graph[j] = append(graph[j], i)
			}
		}
	}
	for i := 0; i < n; i++ {
		queue, cur, explored := []int{i}, 0, make([]bool, n)
		explored[i] = true
		for len(queue) > 0 {
			node := queue[0]
			queue = queue[1:]
			cur++
			for _, nxt := range graph[node] {
				if !explored[nxt] {
					explored[nxt] = true
					queue = append(queue, nxt)
				}
			}
		}
		ans = max(ans, cur)
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var bombs [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &bombs); err != nil {
		log.Fatal(err)
	}

	return maximumDetonation(bombs)
}
