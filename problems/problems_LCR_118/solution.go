package problemLCR_118

import (
	"encoding/json"
	"log"
	"strings"
)

func findRedundantConnection(edges [][]int) []int {
	graph := make(map[int][]int)
	degree := make(map[int]int)
	for _, edge := range edges {
		graph[edge[0]] = append(graph[edge[0]], edge[1])
		graph[edge[1]] = append(graph[edge[1]], edge[0])
		degree[edge[0]]++
		degree[edge[1]]++
	}
	n := len(graph)
	var dequeue []int
	for k, v := range degree {
		if v == 1 {
			dequeue = append(dequeue, k)
		}
	}
	excluded := make(map[int]any)
	for len(dequeue) > 0 {
		node := dequeue[0]
		dequeue = dequeue[1:]
		for _, neighbor := range graph[node] {
			degree[neighbor]--
			if degree[neighbor] == 1 {
				dequeue = append(dequeue, neighbor)
			}
			excluded[min(node, neighbor)*n+max(node, neighbor)] = nil
		}
	}
	for i := len(edges) - 1; i >= 0; i-- {
		if _, ok := excluded[min(edges[i][0], edges[i][1])*n+max(edges[i][0], edges[i][1])]; !ok {
			return edges[i]
		}
	}
	return nil
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var edges [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &edges); err != nil {
		log.Fatal(err)
	}

	return findRedundantConnection(edges)
}
