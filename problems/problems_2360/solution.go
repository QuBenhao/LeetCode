package problem2360

import (
	"encoding/json"
	"log"
	"strings"
)

func longestCycle(edges []int) (ans int) {
	n := len(edges)
	visited := make([]int, n)
	ans = -1
	curTime := 1
	for i := range n {
		startTime := curTime // 本轮出发时间
		for i != -1 && visited[i] == 0 {
			visited[i] = curTime
			curTime++
			i = edges[i]
		}
		if i != -1 && visited[i] >= startTime { // 被走过多次的点一定在环内, 环长为最大的时间差
			ans = max(ans, curTime-visited[i])
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var edges []int

	if err := json.Unmarshal([]byte(inputValues[0]), &edges); err != nil {
		log.Fatal(err)
	}

	return longestCycle(edges)
}
