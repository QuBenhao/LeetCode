package problem2359

import (
	"encoding/json"
	"log"
	"strings"
)

func closestMeetingNode(edges []int, node1 int, node2 int) int {
	dfs := func(node int, dis []int) {
		d := 0
		for cur := node; cur != -1 && dis[cur] == -1; cur = edges[cur] {
			dis[cur] = d
			d++
		}
	}
	n := len(edges)
	dis1 := make([]int, n)
	dis2 := make([]int, n)
	for i := range n {
		dis1[i] = -1
		dis2[i] = -1
	}
	dfs(node1, dis1)
	dfs(node2, dis2)
	ans, ansD := -1, 0x3f3f3f3f
	for i := range n {
		if dis1[i] == -1 || dis2[i] == -1 {
			continue
		}
		if d := max(dis1[i], dis2[i]); d < ansD {
			ansD = d
			ans = i
		}
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var edges []int
	var node1 int
	var node2 int

	if err := json.Unmarshal([]byte(inputValues[0]), &edges); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &node1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &node2); err != nil {
		log.Fatal(err)
	}

	return closestMeetingNode(edges, node1, node2)
}
