package problem1184

import (
	"encoding/json"
	"log"
	"strings"
)

func distanceBetweenBusStops(distance []int, start int, destination int) int {
	n, mn, mx := len(distance), min(start, destination), max(start, destination)
	clock, clockwise := 0, 0
	for i := mn; i < mx; i++ {
		clock += distance[i]
	}
	for i := mx; i < mn+n; i++ {
		clockwise += distance[i%n]
	}
	return min(clock, clockwise)
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var distance []int
	var start int
	var destination int

	if err := json.Unmarshal([]byte(inputValues[0]), &distance); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &start); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &destination); err != nil {
		log.Fatal(err)
	}

	return distanceBetweenBusStops(distance, start, destination)
}
