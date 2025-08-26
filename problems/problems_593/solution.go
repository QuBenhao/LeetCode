package problem593

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func validSquare(p1 []int, p2 []int, p3 []int, p4 []int) bool {
	distance := func(a, b []int) int {
		return (a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1])
	}
	distances := []int{
		distance(p1, p2), distance(p1, p3), distance(p1, p4),
		distance(p2, p3), distance(p2, p4), distance(p3, p4),
	}
	sort.Ints(distances)
	return distances[0] > 0 && distances[0] == distances[1] &&
		distances[0] == distances[2] && distances[0] == distances[3] &&
		distances[4] == distances[5] && distances[4] == 2*distances[0]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var p1 []int
	var p2 []int
	var p3 []int
	var p4 []int

	if err := json.Unmarshal([]byte(inputValues[0]), &p1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &p2); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &p3); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &p4); err != nil {
		log.Fatal(err)
	}

	return validSquare(p1, p2, p3, p4)
}
