package problem2374

import (
	"encoding/json"
	"log"
	"strings"
)

func edgeScore(edges []int) (ans int) {
	n := len(edges)
	counter := make([]int, n)
	for i, edge := range edges {
		counter[edge] += i
		if counter[edge] > counter[ans] {
			ans = edge
		} else if counter[edge] == counter[ans] && edge < ans {
			ans = edge
		}
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var edges []int

	if err := json.Unmarshal([]byte(inputValues[0]), &edges); err != nil {
		log.Fatal(err)
	}

	return edgeScore(edges)
}
