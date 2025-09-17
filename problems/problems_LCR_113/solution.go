package problemLCR_113

import (
	"encoding/json"
	"log"
	"strings"
)

func findOrder(numCourses int, prerequisites [][]int) (ans []int) {
	degree := make([]int, numCourses)
	children := make(map[int][]int)
	for _, prerequisite := range prerequisites {
		degree[prerequisite[0]]++
		children[prerequisite[1]] = append(children[prerequisite[1]], prerequisite[0])
	}
	var q []int
	for i, c := range degree {
		if c == 0 {
			q = append(q, i)
		}
	}
	for len(q) > 0 {
		node := q[0]
		ans = append(ans, node)
		q = q[1:]
		for _, child := range children[node] {
			degree[child]--
			if degree[child] == 0 {
				q = append(q, child)
			}
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var numCourses int
	var prerequisites [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &numCourses); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &prerequisites); err != nil {
		log.Fatal(err)
	}

	return findOrder(numCourses, prerequisites)
}
