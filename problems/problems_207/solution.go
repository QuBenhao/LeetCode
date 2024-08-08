package problem207

import (
	"encoding/json"
	"log"
	"strings"
)

func canFinish(numCourses int, prerequisites [][]int) bool {
	dg := make([]int, numCourses)
	graph := map[int][]int{}
	for _, req := range prerequisites {
		a, b := req[0], req[1]
		dg[a] += 1
		graph[b] = append(graph[b], a)
	}
	var q []int
	for i, d := range dg {
		if d == 0 {
			q = append(q, i)
		}
	}
	explored := 0
	for len(q) > 0 {
		first := q[0]
		q = q[1:]
		explored++
		for _, other := range graph[first] {
			dg[other]--
			if dg[other] == 0 {
				q = append(q, other)
			}
		}
	}
	return explored == numCourses
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var numCourses int
	var prerequisites [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &numCourses); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &prerequisites); err != nil {
		log.Fatal(err)
	}

	return canFinish(numCourses, prerequisites)
}
