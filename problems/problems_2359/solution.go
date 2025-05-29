package problem2359

import (
	"encoding/json"
	"log"
	"strings"
)

func closestMeetingNode(edges []int, node1 int, node2 int) int {
    
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
